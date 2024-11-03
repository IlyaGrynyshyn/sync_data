from env import env

CONNECTION = {
    "driver": "postgresql+asyncpg",
    "host": env("DB_HOST"),
    "port": env("DB_PORT"),
    "username": env("DB_USERNAME"),
    "password": env("DB_PASSWORD"),
    "database": env("DB_NAME"),
    "schema": "public",
}


CREATE_IF_NOT_EXIST = [
    # "cnap.Cnap",
    "cnap_report.CnapReport",
    # "ova.Ova"
]
