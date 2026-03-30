from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    table_name: str
    aws_region: str
    s3_bucket_name: str 
    cognito_user_pool_id: str
    cognito_client_id: str
    environment: str = "dev"


app_config = Setting()


