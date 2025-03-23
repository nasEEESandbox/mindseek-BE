from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    nip: str
    role: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: Optional[EmailStr] = None
    nip: Optional[str] = None
    password: str

    @model_validator()
    def validate_credentials(self, v):
        if not v.email and not v.nip:
            raise ValueError("Email or NIP is required")
        return v

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str

    class Config:
        orm_mode = True