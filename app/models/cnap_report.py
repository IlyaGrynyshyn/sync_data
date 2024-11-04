from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID

from app.models.model import Model


class CnapReport(Model):
    __tablename__ = "cnap_reports"

    id = Column(UUID(as_uuid=True), primary_key=True)

    asc_org_idf = Column(String, unique=True, nullable=False)
    asc_org_name = Column(String, nullable=False)
    asc_org_address = Column(JSON, nullable=False)
    general_data = Column(JSON, nullable=False)
    activity_data = Column(JSON, nullable=False)
    info_support_data = Column(JSON, nullable=False)
    admin_service_data = Column(JSON, nullable=False)
    resp_person_data = Column(JSON, nullable=False)
