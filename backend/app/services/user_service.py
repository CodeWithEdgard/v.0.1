from os import name
from sqlalchemy.orm import Session

from app.db.schema import User
from app.models.users import UserCreate


class UserService:

    def __init__(self, session: Session):
        self.db = session

    def list_users(self) -> list[User]:
        return self.db.query(User).all()

    def create_user(self, name: str) -> User:
            user = User(name=name)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
