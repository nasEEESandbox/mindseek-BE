from pydantic import BaseModel, EmailStr
from datetime import date

from typing import List, Optional

from app.schemas.psychiatrist_availability import PsychiatristAvailabilityCreate, PsychiatristAvailabilityResponse
from app.utils.constant import Gender


class PsychiatristResponse(BaseModel):
    id: int
    display_id: str | None
    email: EmailStr | None
    government_id: str | None
    name: str | None
    gender: Gender | None
    dob: date | None
    nip: str | None
    phone_number: str | None
    license_number: str | None
    specialization: str | None
    consultation_fee: str | None
    age: int | None
    photo_url: str | None
    availability: List[PsychiatristAvailabilityResponse]

    class Config:
        orm_mode = True

class PsychiatristCreate(BaseModel):
    government_id: str
    email: EmailStr
    name: str
    password: str
    gender: Gender
    dob: date
    phone_number: str
    license_number: str
    specialization: str
    consultation_fee: str
    availability: List[PsychiatristAvailabilityCreate]

class PsychiatristUpdate(BaseModel):
    email: EmailStr | None
    nip: str | None
    government_id: str | None
    display_id: str | None
    name: str | None
    gender: Gender | None
    dob: date | None
    phone_number: str | None
    license_number: str | None
    specialization: str | None
    consultation_fee: str | None

