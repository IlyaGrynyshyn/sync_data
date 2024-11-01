from app.models.model import Model
from sqlalchemy import Column, Integer, Date
from sqlalchemy.dialects.postgresql import UUID


class Ova(Model):
    __tablename__ = 'ovas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    ova_id = Column(Integer, unique=True)
    year = Column(Date, nullable=False)
    quarter = Column(Integer, nullable=False)
