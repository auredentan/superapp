from fastapi import FastAPI

from backend.adapters.http import users
from backend.infrastructure.containers.user_container import UserContainer
from backend.adapters.http.api import api_router
from backend.infrastructure.config import Settings


def create_app() -> FastAPI:
    app = FastAPI()

    container = UserContainer()
    container.config.from_pydantic(Settings())
    container.wire(modules=[users])

    app.user_container = container

    app.include_router(api_router, prefix="/v3")
    return app
