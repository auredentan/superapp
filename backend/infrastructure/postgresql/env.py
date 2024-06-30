import asyncio
import os

from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import Connection, pool

from alembic import context
from alembic.config import Config

from backend.adapters.sql.tables.base import Base

# Tables to import
import backend.adapters.sql.tables.user  # noqa: F401


def get_alembic_configuration() -> Config:
    load_dotenv()

    alembic_conf: Config = context.config

    database_url = os.getenv("DATABASE_URL", "NO_DB_URL_FOUND")

    alembic_conf.set_main_option(
        "sqlalchemy.url",
        database_url.replace(
            # alembic allows variable interpolation on %, thus it needs to be escaped by doubling it
            # see https://github.com/sqlalchemy/alembic/issues/700
            "%",
            "%%",
        ),
    )

    return alembic_conf


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations_online())


def do_run_migs(connection: Connection) -> None:
    context.configure(
        connection=connection, target_metadata=[Base.metadata], compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    config = get_alembic_configuration()

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migs)


run_migrations_online()
