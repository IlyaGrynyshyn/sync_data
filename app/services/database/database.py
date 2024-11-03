from typing import Sequence

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import DeclarativeMeta


class DataBaseService:
    def __init__(self, session: AsyncSession, model: type[DeclarativeMeta]):
        self.session = session
        self.model = model

    async def get_all_items(self) -> Sequence[DeclarativeMeta]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def get_item_by_column(self, column: str, condition: str) -> DeclarativeMeta:
        field = getattr(self.model, column)
        result = await self.session.execute(
            select(self.model).where(field == condition)
        )
        return result.scalars().first()

    async def update_record_by_column(
        self, column: str, asc_org_idf: str, update_data: dict
    ) -> None:
        field = getattr(self.model, column)
        stmt = update(self.model).where(field == asc_org_idf).values(**update_data)
        await self.session.execute(stmt)
