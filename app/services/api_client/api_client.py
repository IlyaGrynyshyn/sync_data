from enum import Enum

import httpx

from app.services.log import Log


class Method(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ApiClient:
    log_file: str = "logs/api_client/api_client.log"

    def __init__(self, log_file: str = None):
        if log_file:
            self.log_file = log_file
        self.__init_logger_handler()
        self.logger = Log("report_api_client", self.log_file)
        self.client = httpx.AsyncClient()

    def __init_logger_handler(self):
        self._logger = Log(
            self.log_file.split("/")[-1].replace(".log", ""), self.log_file
        )

    async def get(self, url: str, **kwargs) -> dict:
        return await self.request(Method.GET, url, **kwargs)

    async def post(self, url: str, **kwargs) -> dict:
        return await self.request(Method.POST, url, **kwargs)

    async def request(self, method: Method, url: str, **kwargs) -> dict:
        await self.log_request(method, url, **kwargs)
        try:
            response = await self.client.request(method.value, url, **kwargs)
            response.raise_for_status()
            await self.log_response(method, url, response)
            return response.json()
        except httpx.RequestError as exc:
            await self.logger.error(f"Request error for {exc.request.url}: {exc}")
            return {}
        except httpx.HTTPStatusError as exc:
            await self.logger.error(f"HTTP error: {exc}")
            return {}

    async def log_request(self, method: Method, url: str, **kwargs):
        await self.logger.info(f"Request: {method.value} {url} with params: {kwargs}")

    async def log_response(self, method: Method, url: str, response: httpx.Response):
        await self.logger.info(
            f"Response: {method.value} {url} Status: {response.status_code}"
        )
        if response.is_success:
            await self.logger.info(f"Response data: {response.json()}")
        else:
            await self.logger.error(f"Error response: {response.text}")

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(
        self, exc_type, exc_val, exc_tb
    ):
        await self.close()
