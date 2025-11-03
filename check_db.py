# check_db.py
import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from app.core.config import settings

def main():
    engine = create_engine(settings.database_url, pool_pre_ping=True, future=True)
    attempts = 10
    for i in range(1, attempts + 1):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print(f"[OK] DB reachable on attempt {i}")
            return
        except OperationalError as e:
            print(f"[{i}/{attempts}] DB not ready yet: {e.__class__.__name__}: {e}")
            time.sleep(2)
    print("[FAIL] Could not connect to DB after retries.")

if __name__ == "__main__":
    main()
