import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def run_query(query):
    conn = mysql.connector.connect(
        host=os.getenv("localhost"),
        user=os.getenv("root"),
        password=os.getenv("Gen@@@000"),
        database=os.getenv("fealty_db")
    )
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
