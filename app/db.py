import os
from sqlalchemy import create_engine,text
from sqlalchemy.exc import OperationalError

engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
