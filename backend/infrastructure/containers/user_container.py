from dependency_injector import containers, providers
from backend.adapters.database import create_session_factory
from backend.adapters.repositories.sql.user_repository import SQLAlchemyUserRepository
from backend.services.user_service import UserService


class UserContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_session_factory = providers.Singleton(
        create_session_factory, database_url=config.DATABASE_URL
    )

    user_repository = providers.Factory(
        SQLAlchemyUserRepository, session_factory=db_session_factory
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
