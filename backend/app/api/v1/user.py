from fastapi import APIRouter, Depends

from app.services.user_service import UserService
from app.db.schema import SessionLocal
from app.models.users import UserCreate, UserResponse


router = APIRouter()


def get_user_service() -> UserService:
    return UserService(session=SessionLocal())


@router.get("/users", response_model=list[UserResponse])
def get_users(service: UserService = Depends(get_user_service)):
    return service.list_users()


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user.name)
