from logging.config import fileConfig
from sqlalchemy import create_engine # DB connection when running migrations online
from alembic import context

from app.core.config import settings # importing app configuration
from app.models.user import Base  # contains Base.metadata

config = context.config 

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

# When the DB is offline, Alembic doesn’t apply changes — it only generates SQL scripts.
def run_migrations_offline() -> None:
    url = settings.database_url # get database URL from settings
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# When the DB is online, Alembic actually connects and applies the schema changes.
def run_migrations_online() -> None:
    connectable = create_engine(settings.database_url, pool_pre_ping=True) # checking connection is alive before using it
    with connectable.connect() as connection: # open the DB connection
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
