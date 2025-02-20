from settings import Settings
from setup.ioc import get_container, get_fastapi_app

from dishka.integrations.fastapi import setup_dishka
from uvicorn import run

settings = Settings.from_env()
app = get_fastapi_app(settings)
container = get_container(settings)
setup_dishka(app=app, container=container)
run(app=app, host=settings.host, port=settings.port)
