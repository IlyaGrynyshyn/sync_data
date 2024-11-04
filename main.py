import asyncio
import importlib
import sys
from datetime import timedelta

from loguru import logger


async def execute_command(argv):
    if argv[0] == 'migration':
        logger.add(f"logs/commands/commands.log", rotation=timedelta(weeks=3))
        import commands
        command = getattr(commands, argv[0])
        await command(*argv[1:])
    elif argv[0] == 'process':
        logger.add(f"logs/{argv[0]}/{argv[1]}/{argv[1]}.log", rotation=timedelta(weeks=1))
        logger.info(f'processing {argv[1]}')
        handler = importlib.import_module(f'app.processes.{argv[1]}.main')
        await handler.handler(*argv[2:])


@logger.catch
async def main():
    if (len(sys.argv) <= 1):
        raise ValueError(
            'No valid arguments. First paramet must be command or proccess and name hanler (also support additional params), example: python main.py migration')
    await execute_command(sys.argv[1:])


if __name__ == '__main__':
    asyncio.run(main())