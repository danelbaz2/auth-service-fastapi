import os
import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

url = os.environ.get("DATABASE_URL")
if not url:
    print("❌ DATABASE_URL is not set.", flush=True)
    exit(1)

engine = create_engine(url, pool_pre_ping=True)

for attempt in range(10):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Database connected successfully!", flush=True)
        break
    except OperationalError as e:
        print(f"⏳ Waiting for DB... attempt {attempt+1}/10", flush=True)
        time.sleep(5)
else:
    print("❌ Failed to connect after 10 attempts.", flush=True)
    exit(1)
