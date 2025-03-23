from pydantic import BaseModel, EmailStr
from app.utils.constant import UserRole

# ✅ Schema for Creating an Admin
class AdminCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    nip: str | None

    class Config:
        orm_mode = True

# ✅ Schema for Updating an Admin
class AdminUpdate(BaseModel):
    name: str | None

    class Config:
        orm_mode = True

class AdminResponse(BaseModel):
    id: int
    nip: str | None
    name: str | None
    email: EmailStr
    role: UserRole = UserRole.ADMIN

    class Config:
        from_attributes = True
