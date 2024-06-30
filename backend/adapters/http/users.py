from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from backend.entities.user import User, UserCreate
from backend.services.user_service import UserService
from backend.infrastructure.containers.user_container import UserContainer

router = APIRouter()


@router.post("/", response_model=User)
@inject
def create_user(
    user: UserCreate,
    user_service: UserService = Depends(Provide[UserContainer.user_service]),
):
    return user_service.create_user(user)


@router.get("/{user_id}", response_model=User)
@inject
def read_user(
    user_id: int,
    user_service: UserService = Depends(Provide[UserContainer.user_service]),
):
    return user_service.get_user(user_id)
