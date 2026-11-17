from sqlalchemy import create_engine
from config import DB_CONFIG


def get_connection():

    connection_string = (
        f"oracle+oracledb://"
        f"{DB_CONFIG['username']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/"
        f"?service_name={DB_CONFIG['service_name']}"
    )

    engine = create_engine(connection_string)

    return engine