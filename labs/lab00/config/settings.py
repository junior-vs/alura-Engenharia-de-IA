from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Medical Virtual Assistant"
    OPENAI_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()
