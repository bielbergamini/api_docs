from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Documents API"
    ENV: str = "development"

    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET: str = "documents-api-bucket"
    DYNAMODB_TABLE: str = "documents"

    JWT_SECRET_KEY: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
