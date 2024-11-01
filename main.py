# import uuid
#
# import requests
# import commands
# from app.models.cnap import Cnap
# from app.models.cnap_report import CnapReport
# from app.models.model import Model, ModelMixin
# from app.services.db_service import DataBaseService
# from sqlalchemy.orm import Session
#
#
# # def execute_command(argv):
# #     if argv[0] == "command":
# #         command = getattr(commands, argv[1])
# #         command(*argv[2:])
# #
#
#
# def store_data(session: Session, data_list: list[dict], model):
#     records = []
#     for data in data_list:
#         record = model(
#             id=uuid.uuid4(),
#             asc_org_idf=data['id'],
#             asc_org_name=data["id"],
#             asc_org_address=data["asc_org"],
#             general_data=data["general_data"],
#             activity_data=data["activity_data"],
#             info_support_data=data["info_support_data"],
#             admin_service_data=data["admin_service_data"],
#             resp_person_data=data["resp_person_data"],
#         )
#         records.append(record)
#
#     session.add_all(records)
#     session.commit()
#
#
# def main():
#     url1 = "https://guide.diia.gov.ua/api/v1/static_reports/list/2024/1/?format=json"
#     request = requests.get(url1).json()
#     all_data = []
#
#     for i in request["results"]:
#         id = i["id"]
#         request2 = requests.get(f"https://guide.diia.gov.ua/api/v1/static_reports/entries/{id}?format=json").json()
#         for b in request2["results"]:
#             report_entries_id = b["id"]
#             request3 = requests.get(
#                 f"https://guide.diia.gov.ua/api/v1/static_reports/detail/{report_entries_id}").json()
#             all_data.extend(request3["results"])
#
#     with Session(CnapReport.engine) as session:
#         store_data(session, all_data, CnapReport)
#
#
# main()


# import asyncio
# import httpx
# import uuid
# import time
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.models.cnap_report import CnapReport
#
#
# async def fetch_data(url):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response.json()
#
#
# async def store_data(session: AsyncSession, data_list: list[dict], model):
#     records = []
#     for data in data_list:
#         record = model(
#             id=uuid.uuid4(),
#             asc_org_idf=str(data['id']),
#             asc_org_name=str(data["id"]),
#             asc_org_address=data["asc_org"],
#             general_data=data["general_data"],
#             activity_data=data["activity_data"],
#             info_support_data=data["info_support_data"],
#             admin_service_data=data["admin_service_data"],
#             resp_person_data=data["resp_person_data"],
#         )
#         records.append(record)
#
#     session.add_all(records)
#     await session.commit()
#
#
# async def main():
#     start_time = time.time()  # Записуємо час початку виконання
#
#     url1 = "https://guide.diia.gov.ua/api/v1/static_reports/list/2024/1/?format=json"
#     request = await fetch_data(url1)
#     all_data = []
#
#     async with httpx.AsyncClient() as client:
#         tasks = []
#         for i in request["results"]:
#             id = i["id"]
#             url2 = f"https://guide.diia.gov.ua/api/v1/static_reports/entries/{id}?format=json"
#             tasks.append(fetch_data(url2))
#
#         results = await asyncio.gather(*tasks)
#
#         detail_tasks = []
#         for result in results:
#             for b in result["results"]:
#                 report_entries_id = b["id"]
#                 url3 = f"https://guide.diia.gov.ua/api/v1/static_reports/detail/{report_entries_id}"
#                 detail_tasks.append(fetch_data(url3))
#
#         detail_results = await asyncio.gather(*detail_tasks)
#
#         for result in detail_results:
#             all_data.extend(result["results"])
#
#     async with AsyncSession(CnapReport.engine) as session:
#         await store_data(session, all_data, CnapReport)
#
#     end_time = time.time()  # Записуємо час закінчення виконання
#     elapsed_time = end_time - start_time
#     print(f"Скрипт виконувався {elapsed_time:.2f} секунд.")  # Виводимо час виконання
#
#
# asyncio.run(main())


import asyncio
import httpx
import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cnap_report import CnapReport


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


async def store_data(session: AsyncSession, data_list: list[dict], model):
    records = []
    for data in data_list:
        record = model(
            id=uuid.uuid4(),
            asc_org_idf=str(data['id']),
            asc_org_name=str(data["id"]),
            asc_org_address=data["asc_org"],
            general_data=data["general_data"],
            activity_data=data["activity_data"],
            info_support_data=data["info_support_data"],
            admin_service_data=data["admin_service_data"],
            resp_person_data=data["resp_person_data"],
        )
        records.append(record)

    session.add_all(records)
    await session.commit()


async def main():
    url1 = "https://guide.diia.gov.ua/api/v1/static_reports/list/2024/1/?format=json"
    request = await fetch_data(url1)
    all_data = []

    async with httpx.AsyncClient() as client:
        # Запит на отримання id
        tasks = []
        for i in request["results"]:
            id = i["id"]
            url2 = f"https://guide.diia.gov.ua/api/v1/static_reports/entries/{id}?format=json"

            # Пагінація для отримання даних
            while url2:
                results = await fetch_data(url2)
                tasks.extend(results["results"])
                url2 = results["next"]  # отримуємо URL для наступної сторінки

        detail_tasks = []
        for result in tasks:
            report_entries_id = result["id"]
            url3 = f"https://guide.diia.gov.ua/api/v1/static_reports/detail/{report_entries_id}"
            detail_tasks.append(fetch_data(url3))

        detail_results = await asyncio.gather(*detail_tasks)

        for result in detail_results:
            all_data.extend(result["results"])

    async with AsyncSession(CnapReport.engine) as session:
        await store_data(session, all_data, CnapReport)


asyncio.run(main())