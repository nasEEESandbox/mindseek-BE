from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.auth import AuthLogin, AuthUpdatePassword, AuthRegister, AuthResponse
from app.db.models.psychiatrist import Psychiatrist
from app.core.security import get_password_hash, verify_password
from app.utils.constant import generate_nip

router = APIRouter()

@router.post("/register", response_model=AuthResponse)
def register_user(user_data: AuthRegister, db: Session = Depends(get_db)):
    existing_user = None
    if user_data.email:
        existing_user = db.query(Psychiatrist).filter(Psychiatrist.email == user_data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    nip = generate_nip()
    print('nip', nip)
    existing_nip = db.query(Psychiatrist).filter(Psychiatrist.nip == nip).first()
    while existing_nip:
        nip = generate_nip()
        existing_nip = db.query(Psychiatrist).filter(Psychiatrist.nip == nip).first()

    new_user = Psychiatrist(
        email=str(user_data.email),
        nip=nip,
        hashed_password=get_password_hash(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=AuthResponse)
def login_user(user: AuthLogin, db: Session = Depends(get_db)):
    if (user.email and user.nip) or (not user.email and not user.nip):
        raise HTTPException(status_code=400, detail="Either email or nip must be provided")
    if user.email:
        db_user = db.query(Psychiatrist).filter(Psychiatrist.email == user.email).first()
    else:
        db_user = db.query(Psychiatrist).filter(Psychiatrist.nip == user.nip).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return db_user

@router.put("/change-password", response_model=AuthResponse)
def change_password(user: AuthUpdatePassword, db: Session = Depends(get_db)):
    if (user.email and user.nip) or (not user.email and not user.nip):
        raise HTTPException(status_code=400, detail="Either email or nip must be provided")

    if user.new_password != user.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirm password do not match")

    db_user = None
    if user.email:
        db_user = db.query(Psychiatrist).filter(Psychiatrist.email == user.email).first()
    if user.nip:
        db_user = db.query(Psychiatrist).filter(Psychiatrist.nip == user.nip).first()

    if user.password and not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.hashed_password = get_password_hash(user.new_password)
    db.commit()
    db.refresh(db_user)

    return db_user
