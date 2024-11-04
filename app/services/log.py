import asyncio

from loguru import logger


class Log:
    def __init__(self, name: str, log_file: str):
        self.name = name
        self.log_file = log_file
        logger.add(self.log_file)

    async def log(self, message: str, level: str = "INFO"):
        await asyncio.sleep(
            0
        )
        logger.log(level, message)

    async def info(self, message: str):
        await self.log(message, level="INFO")

    async def error(self, message: str):
        await self.log(message, level="ERROR")
