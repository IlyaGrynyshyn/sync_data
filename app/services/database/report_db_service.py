import uuid

from app.services.database.database import DataBaseService


class ReportDBService(DataBaseService):
    async def upsert_records(self, data_list: list) -> None:
        for data in data_list:
            asc_org_idf = data["asc_org"]["idf"]
            existing_record = await self.get_item_by_column("asc_org_idf", asc_org_idf)

            if existing_record:
                update_data = self._prepare_record_data(data, is_update=True)
                await self.update_record_by_column(
                    "asc_org_idf", asc_org_idf, update_data
                )
            else:
                new_record_data = self._prepare_record_data(data, is_update=False)
                new_record = self.model(**new_record_data)
                self.session.add(new_record)

        await self.session.commit()

    def _prepare_record_data(self, data: dict, is_update: bool) -> dict:
        record_data = {
            "asc_org_idf": str(data["asc_org"]["idf"]),
            "asc_org_name": str(data["asc_org"]["name"]),
            "asc_org_address": data["asc_org"]["address"],
            "general_data": data["general_data"],
            "activity_data": data["activity_data"],
            "info_support_data": data["info_support_data"],
            "admin_service_data": data["admin_service_data"],
            "resp_person_data": data["resp_person_data"],
        }

        if not is_update:
            record_data["id"] = uuid.uuid4()

        return record_data
