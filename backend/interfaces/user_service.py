from abc import ABC, abstractmethod
from backend.entities.user import User
from backend.entities.user import UserCreate

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, user: UserCreate) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass
