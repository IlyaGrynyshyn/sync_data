import importlib
from loguru import logger
from config.database import CREATE_IF_NOT_EXIST


def migration():
    for model_path in CREATE_IF_NOT_EXIST:
        model_file = ".".join(model_path.split(".")[:-1])
        model_class = model_path.split(".")[-1]
        model_module = importlib.import_module(f"app.models.{model_file}")
        table = getattr(model_module, model_class)
        table.__table__.create(bind = table.engine, checkfirst = True)

    logger.success("Migration complete")


migration()