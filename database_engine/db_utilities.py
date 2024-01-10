from sqlalchemy import create_engine, Engine
"""
TODO:
solve how to have many users with the same username and password
"""


def get_connection(us_name: str, us_pass: str, db_name: str, port: int,version: str) -> Engine:
    if version == "local":
        host = "127.0.0.1"
    else:
        host = "host_database"
    return f"mysql+pymysql://{us_name}:{us_pass}@{host}:{port}/{db_name}"# create_engine()