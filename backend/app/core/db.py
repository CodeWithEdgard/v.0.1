from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.domains.usuarios.models import Usuario

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/app"

engine = create_engine(DATABASE_URL)

localSession = sessionmaker(bind=engine)


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

Base.metadata.create_all(bind=engine)
