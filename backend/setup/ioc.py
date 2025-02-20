from presentation.main import main_router
from settings import Settings

from .providers.auth import AuthProvider
from .providers.main import MainProvider
from .providers.persistence import PersistenceProvider

from dishka import AsyncContainer, make_async_container
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_container(settings: Settings) -> AsyncContainer:
    return make_async_container(PersistenceProvider(), MainProvider(), AuthProvider(), context={Settings: settings})


def get_fastapi_app(settings: Settings) -> FastAPI:
    app = FastAPI(title='Shadowcut', description='A simple link shortcut management application', version='1.0.0')
    app.include_router(main_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    return app
