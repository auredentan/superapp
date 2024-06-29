from fastapi import APIRouter
from backend.adapters.http import users
from backend.infrastructure.containers.user_container import UserContainer

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])


