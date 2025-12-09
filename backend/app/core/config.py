from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "v.0.1"
    debug: bool = False
    db_user: str = ""
    db_password: str = ""
    db_name: str = ""
    DB_URL: str = ""


config = Config()
