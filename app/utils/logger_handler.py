from app.services.log import Log


def init_logger_handler(log_file: str):
    return Log(log_file.split("/")[-1].replace(".log", ""), log_file)
