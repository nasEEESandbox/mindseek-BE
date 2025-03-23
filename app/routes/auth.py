from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserResponse, UserCreate, UserLogin
from app.db.models.user import User
from app.core.security import get_password_hash, verify_password

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email is already registered
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create User object
    db_user = User(
        email=str(user.email),
        hashed_password=get_password_hash(user.password),
        role=user.role,  # Assign the selected role (PATIENT, PSYCHIATRIST, ADMIN)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.post("/login", response_model=UserResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    if (user.email and user.nip) or (not user.email and not user.nip):
        raise HTTPException(status_code=400, detail="Either email or nip must be provided")

    if user.email:
        db_user = db.query(User).filter(User.email == user.email).first()
    else:
        db_user = db.query(User).filter(User.nip == user.nip).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return db_user