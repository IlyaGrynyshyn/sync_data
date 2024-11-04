from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declared_attr, DeclarativeBase

from config.database import CONNECTION


class ModelMixin:
    @declared_attr
    def connection_string(cls):
        return f'{CONNECTION["driver"]}://{CONNECTION["username"]}:{CONNECTION["password"]}@{CONNECTION["host"]}:{CONNECTION["port"]}/{CONNECTION["database"]}'

    @declared_attr
    def engine(cls):
        return create_async_engine(cls.connection_string)


class Model(ModelMixin, DeclarativeBase):
    ...
