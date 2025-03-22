from pydantic import BaseModel, EmailStr
from app.db.models.user import User
from app.db.models.patient import Patient
from app.db.models.psychiatrist import Psychiatrist

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str

class PatientUpdate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str