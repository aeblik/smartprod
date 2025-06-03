import psycopg2
import os
import time

MAX_RETRIES = 10
RETRY_DELAY = 2  # seconds

def connect_to_db():
    for i in range(MAX_RETRIES):
        try:
            conn = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST'),
                database=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD')
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"DB not ready (attempt {i+1}/{MAX_RETRIES}), retrying in {RETRY_DELAY}s...")
            time.sleep(RETRY_DELAY)
    raise Exception("Could not connect to database after several retries.")

# Connect
conn = connect_to_db()

# Auto-create table if it doesn't exist
def init_db():
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id SERIAL PRIMARY KEY,
                filename TEXT,
                file_url TEXT,
                upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()

init_db()

# Regular insert/query functions
def insert_file_metadata(filename, file_url):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO files (filename, file_url) VALUES (%s, %s)", (filename, file_url))
        conn.commit()

def get_all_files():
    with conn.cursor() as cur:
        cur.execute("SELECT filename, file_url, upload_time FROM files ORDER BY upload_time DESC")
        return cur.fetchall()
