from logging.config import fileConfig
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from adapters.models.base import BaseModel
from adapters.models.shortcut import ShortcutModel  # type: ignore
from settings import Settings

from alembic import context
from sqlalchemy import engine_from_config, pool


def add_query_arg(url: str, arg_name: str, arg_value: str):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params[arg_name] = [arg_value]
    new_query_string = urlencode(query_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query_string))

    return new_url


config = context.config
settings = Settings.from_env()


config.set_main_option('sqlalchemy.url', add_query_arg(settings.database_dsn, 'async_fallback', 'True'))


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = BaseModel.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option('sqlalchemy.url')

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    from sqlalchemy_utils import types

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
