import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.pagination import PaginationParams
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services import user_service

router = APIRouter(prefix="/users", tags=["users"])


# Success: 201
# DTO: UserResponse, UserCreate
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # Auth / parameter validation # per condition
    return user_service.create_user(db, user_in)

# Success: 200
@router.get("/", response_model=list[UserResponse])
def list_users(
    pagination: Annotated[PaginationParams, Query()], db: Session = Depends(get_db)
):
    return user_service.get_users(db, pagination.skip, pagination.limit)

# Request Path
# Example: /users/1
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)

# 404 (Not found)
# 4xx (Denial category)
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: uuid.UUID, user_in: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user_in)

# 200 (50%), 204 (50%)
# 2XX (Success)
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
