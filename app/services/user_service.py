import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories import user_repository
from app.schemas.user import UserCreate, UserUpdate

# Business logic will be written in service layer

def create_user(db: Session, user_in: UserCreate) -> User:
    if user_repository.get_by_email(db, user_in.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already registered"
        )

    user = User(email=user_in.email, hashed_password=hash_password(user_in.password))
    return user_repository.create(db, user)


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return user_repository.list(db, skip, limit)


def get_user(db: Session, user_id: uuid.UUID) -> User:
    user = user_repository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def update_user(db: Session, user_id: uuid.UUID, user_in: UserUpdate) -> User:
    user = get_user(db, user_id)

    if user_in.email is not None:
        user.email = user_in.email
    if user_in.password is not None:
        user.hashed_password = hash_password(user_in.password)
    if user_in.is_active is not None:
        user.is_active = user_in.is_active

    return user_repository.update(db, user)


def delete_user(db: Session, user_id: uuid.UUID) -> None:
    user = get_user(db, user_id)
    user_repository.delete(db, user)
