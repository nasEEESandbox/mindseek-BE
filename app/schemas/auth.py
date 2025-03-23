from pydantic import BaseModel, EmailStr, model_validator

class AuthResponse(BaseModel):
    email: EmailStr
    nip: str
    is_admin: bool

    class Config:
        orm_mode = True

class AuthLogin(BaseModel):
    email: EmailStr | None
    nip: str | None
    password: str

    @model_validator(mode="before")
    def validate_credentials(self, values):
        email = values.get("email")
        nip = values.get("nip")

        if not email and not nip:
            raise ValueError("Either Email or NIP is required")

        return values

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