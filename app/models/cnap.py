from sqlalchemy.orm import relationship

from app.models.model import Model
from sqlalchemy import Column, Integer, Date
from sqlalchemy.dialects.postgresql import UUID

from app.models.ova import Ova


class Cnap(Model):
    __tablename__ = 'cnap'

    id = Column(UUID(as_uuid=True), primary_key=True)
    cnap_id = Column(Integer, nullable=False)

    ova_id = relationship(Ova)


