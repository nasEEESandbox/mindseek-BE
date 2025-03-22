from pydantic import BaseModel, EmailStr

# Response model (to hide password)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True  # Enable ORM mode

class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str

class PatientUpdate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    