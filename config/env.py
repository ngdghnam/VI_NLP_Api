from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    GOOGLE_CUSTOM_SEARCH_API_KEY: str
    CUSTOM_SEARCH_ENGINE_ID: str
    BACKUP_CUSTOM_SEARCH_API_KEY: str
    DB_HOST: str  
    DB_PORT: int 
    DB_USER: str 
    DB_NAME: str 
    DB_PASSWORD: str  
    GOOGLE_CUSTOM_SEARCH_API_KEY: str 
    DB_DIALECT: str
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()