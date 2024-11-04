from datetime import datetime, time
from time import perf_counter
from loguru import logger
import psutil

from app.utils.logger_handler import init_logger_handler

loger_file = (
    f"logs/cpu_benchmark/report_{datetime.today().strftime('%Y-%m-%d')}"
)
log = init_logger_handler(loger_file)


def benchmark(func):
    async def wrapper(*args, **kwargs):
        start_time = perf_counter()
        start_cpu = psutil.cpu_percent(interval=None)
        start_memory = psutil.Process().memory_info().rss / (1024 * 1024)

        result = await func(*args, **kwargs)

        end_time = perf_counter()
        end_cpu = psutil.cpu_percent(interval=None)
        end_memory = psutil.Process().memory_info().rss / (1024 * 1024)

        elapsed_time = end_time - start_time
        cpu_usage = end_cpu - start_cpu
        memory_usage = end_memory - start_memory

        await log.info(
            f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds, "
            f"CPU usage change: {cpu_usage:.2f}%, Memory usage change: {memory_usage:.2f} MB"
        )
        return result

    return wrapper
