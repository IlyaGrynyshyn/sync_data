# from loguru import logger
# from dataclasses import dataclass
# from collections import namedtuple
#
#
#
#
# def get_level(level_name: str):
#     return logger._core.levels.get(level_name)
#
#
#
# all_names = []
#
# standard_levels = [
#     get_level('TRACE'),
#     get_level('DEBUG'),
#     get_level('INFO'),
#     get_level('SUCCESS'),
#     get_level('WARNING'),
#     get_level('ERROR'),
#     get_level('CRITICAL')
# ]
#
# Level = namedtuple('Level', ['name', 'no', 'color', 'icon'])
#
#
# @dataclass
# class Levels:
#     TRACE: Level
#     DEBUG: Level
#     INFO: Level
#     SUCCESS: Level
#     WARNING: Level
#     ERROR: Level
#     CRITICAL: Level
#
#
# class Log:
#     __general: bool
#     __logger_levels: Levels
#     __name: str
#     __log_file: str
#     __daily: bool
#
#     def __init__(self, name: str, log_file: str = None):
#         self.__set_name(name)
#         self.__set_log_file(log_file)
#
#
#     def __set_log_file(self, log_file: str = None):
#         if log_file is None:
#             log_file = f'logs/{self.__name}'
#
#         if '.log' in log_file:
#             log_file = log_file.replace('.log', '')
#
#         if self.__daily:
#             log_file += '_{time:YYYY-MM-DD}'
#
#         self.__log_file = f'{log_file}.log'
#
#     def __set_name(self, name):
#         if name in all_names:
#             raise ValueError(f'Log "{name}" already exist!')
#         self.__name = name
#         all_names.append(name)
#
#     def __init_general(self):
#         logger_levels = {standard_level.name: standard_level.no for standard_level in standard_levels}
#         self.__logger_levels = Levels(**logger_levels)
#
#         self.__logger_add()
#
#
#     def __logger_add(self, **kwargs):
#         logger.add(self.__log_file, **kwargs)
#
#     def trace(self, message: str):
#         self.log(message, self.__logger_levels.TRACE)
#
#     def debug(self, message: str):
#         self.log(message, self.__logger_levels.DEBUG)
#
#     def info(self, message: str):
#         self.log(message, self.__logger_levels.INFO)
#
#     def success(self, message: str):
#         self.log(message, self.__logger_levels.SUCCESS)
#
#     def warning(self, message: str):
#         self.log(message, self.__logger_levels.WARNING)
#
#     def error(self, message: str):
#         self.log(message, self.__logger_levels.ERROR)
#
#     def critical(self, message: str):
#         self.log(message, self.__logger_levels.CRITICAL)
#
#     def log(self, message: str, level: Level = None):
#         if level is None:
#             level = self.__logger_levels.INFO
#
#         logger.log(level.name, message)
#

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
        )  # дозволяє повернути управління подіями, якщо виклик асинхронний
        logger.log(level, message)

    async def info(self, message: str):
        await self.log(message, level="INFO")

    async def error(self, message: str):
        await self.log(message, level="ERROR")
