from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserResponse
from app.db.models.user import User

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# @router.put("/{user_id}", response_model=UserResponse)
# def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     for key, value in user.dict().items():
#         setattr(db_user, key, value)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

