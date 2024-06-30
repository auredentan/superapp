from abc import ABC, abstractmethod
from backend.entities.user import User
from backend.entities.user import UserCreate


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: UserCreate) -> User:
        pass

    @abstractmethod
    def get(self, user_id: int) -> User | None:
        pass
