from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MyApp"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

