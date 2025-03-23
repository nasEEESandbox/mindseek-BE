from pydantic import BaseModel, EmailStr, model_validator

class AuthResponse(BaseModel):
    email: EmailStr
    nip: str
    is_admin: bool

    class Config:
        orm_mode = True

class AuthLogin(BaseModel):
    email: str | None
    nip: str | None
    password: str

    @model_validator(mode="before")
    def validate_credentials(cls, data):
        data = data.data if hasattr(data, "data") else data  # ✅ Fix for Pydantic v2
        email = data.get("email")
        nip = data.get("nip")

        if not email and not nip:
            raise ValueError("Either Email or NIP is required")

        return data

    class Config:
        orm_mode = True

class AuthRegister(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class AuthUpdatePassword(BaseModel):
    email: EmailStr | None
    nip: str | None
    password: str | None
    new_password: str
    confirm_password: str

    class Config:
        orm_mode = True