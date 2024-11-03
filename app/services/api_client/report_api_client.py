import asyncio
from time import time

import httpx

from app.services.api_client.api_client import ApiClient
from app.utils.get_prev_quarter import get_previous_quarter


class ReportApiClient(ApiClient):
    def __init__(self, log_file=None):
        super().__init__(log_file=log_file),
        self.semaphore = asyncio.Semaphore(30)

    async def fetch_data(self, url: str, client) -> dict:
        async with self.semaphore:
            start_time = time()
            try:
                response = await client.get(url, timeout=10)
                response.raise_for_status()
                await self.logger.info(
                    f"Fetched data from {url} in {time() - start_time:.2f} seconds"
                )
                return response.json()
            except httpx.RequestError as exc:
                await self.logger.error(f"Request error for {exc.request.url}: {exc}")
                return {}
            except httpx.HTTPStatusError as exc:
                await self.logger.error(f"HTTP error: {exc}")
                return {}

    async def fetch_report(self) -> list:
        year, quarter = get_previous_quarter()
        url1 = f"https://guide.diia.gov.ua/api/v1/static_reports/list/{year}/{quarter}/?format=json"
        async with httpx.AsyncClient() as client:
            request = await self.fetch_data(url1, client)
            all_data = []

            tasks = []
            for i in request.get("results", []):
                id = i["id"]
                url2 = f"https://guide.diia.gov.ua/api/v1/static_reports/entries/{id}?format=json"
                while url2:
                    results = await self.fetch_data(url2, client)
                    tasks.extend(results.get("results", []))
                    url2 = results.get("next")

            detail_tasks = []
            for result in tasks:
                report_entries_id = result["id"]
                url3 = f"https://guide.diia.gov.ua/api/v1/static_reports/detail/{report_entries_id}"
                detail_tasks.append(self.fetch_data(url3, client))

            detail_results = await asyncio.gather(*detail_tasks)

            for result in detail_results:
                if result:
                    all_data.extend(result.get("results", []))
        return all_data
