from datetime import datetime
from time import time

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cnap_report import CnapReport
from app.services.api_client.report_api_client import ReportApiClient
from app.services.database.report_db_service import ReportDBService
from app.utils.logger_handler import init_logger_handler

loger_file = (
    f"logs/api_client/report_client/report_{datetime.today().strftime('%Y-%m-%d')}"
)
log = init_logger_handler(loger_file)


async def get_cnap_reports():
    start_time = time()
    report_client = ReportApiClient(log_file=loger_file)
    all_data = await report_client.fetch_report()
    async with AsyncSession(CnapReport.engine) as session:
        session.expire_on_commit = False
        db_service = ReportDBService(session, CnapReport)

        await db_service.upsert_records(all_data)

    await log.info(f"Script executed in {time() - start_time:.2f} seconds")


async def handler(*args):
    await get_cnap_reports()