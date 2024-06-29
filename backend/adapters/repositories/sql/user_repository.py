from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Callable
from backend.entities.user import User
from backend.entities.user import UserCreate
from backend.interfaces.user_repository import UserRepositoryInterface

class SQLAlchemyUserRepository(UserRepositoryInterface):
    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory

    def create(self, user: UserCreate) -> User:
        with self.session_factory() as session:
            db_user = User(email=user.email, id=1)  # In a real app, hash the password
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            return db_user

    def get(self, user_id: int) -> User | None:
        with self.session_factory() as session:
            query = select(User).filter(User.id == user_id)
            return session.scalars(query).first()
