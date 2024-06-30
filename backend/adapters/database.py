from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_session_factory(database_url: str):
    engine = create_engine(database_url)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
