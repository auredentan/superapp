from backend.interfaces.user_service import UserServiceInterface
from backend.interfaces.user_repository import UserRepositoryInterface
from backend.entities.user import User
from backend.entities.user import UserCreate


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> User:
        return self.user_repository.create(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get(user_id)
