from db_connection import get_connection
from sqlalchemy import text
import pandas as pd

engine = get_connection()

with engine.connect() as conn:

    result = conn.execute(
        text("SELECT 'Oracle Connected' FROM DUAL")
    )

    print(result.fetchone())

query = """
SELECT *
FROM EMPLOYEES
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.columns.tolist())

engine.dispose()