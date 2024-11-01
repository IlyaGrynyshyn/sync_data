import commands
from app.models.cnap import Cnap
from app.models.model import Model, ModelMixin
from app.services.db_service import DataBaseService


def execute_command(argv):
    if argv[0] == "command":
        command = getattr(commands, argv[1])
        command(*argv[2:])


def main():
    ...

