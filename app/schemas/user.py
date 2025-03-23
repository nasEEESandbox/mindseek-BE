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

    @model_validator(mode="before")  # ✅ Correct mode
    def validate_credentials(self, values):
        email = values.get("email")
        nip = values.get("nip")

        if not email and not nip:
            raise ValueError("Either Email or NIP is required")

        return values

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str

    class Config:
        orm_mode = True

class UserUpdatePassword(BaseModel):
    email: EmailStr | None
    nip: str | None
    password: str | None
    new_password: str
    confirm_password: str

    class Config:
        orm_mode = True