from fastapi import FastAPI
from app.core.config import config

from app.core.logging import setup_logging
from app.db.schema import Base, engine
from app.api.v1.user import router as user_router

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.app_name)

app.include_router(user_router, prefix="/api/v1")
