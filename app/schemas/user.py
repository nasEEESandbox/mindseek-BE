from pydantic import BaseModel, EmailStr

# Request model for user creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Response model (to hide password)
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # Enable ORM mode
