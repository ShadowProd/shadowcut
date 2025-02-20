from typing import Annotated, Self

from pydantic import AnyHttpUrl, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    cors_origins: list[Annotated[str, AnyHttpUrl]]

    database_dsn: Annotated[str, PostgresDsn]

    admin_key: str

    @classmethod
    def from_env(cls, path: str = '.env') -> Self:
        return cls(_env_file=path)  # type: ignore
