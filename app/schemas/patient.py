from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List

from app.utils.constant import Gender


class PatientResponse(BaseModel):
    id: int | None
    display_id: str | None
    email: EmailStr | None
    government_id: str | None
    name: str | None
    dob: date | None
    gender: Gender | None
    phone_number: str | None
    blood_group: str | None
    marital_status: str | None
    occupation: str | None
    insurance_provider: str | None
    address: str | None
    emergency_contact_name: str | None
    emergency_contact_number: str | None
    emergency_contact_relationship: str | None
    psychiatrist_id: int | None
    appointment_ids: List[int] | None
    latest_diagnosis_id: int | None
    latest_medication_id: int | None
    photo_url: str | None

    class Config:
        from_attributes = True


class PatientCreate(BaseModel):
    email: EmailStr
    display_id: str
    government_id: str
    name: str
    dob: date
    gender: Gender
    phone_number: str
    blood_group: str
    marital_status: str
    occupation: str
    insurance_provider: str
    address: str
    emergency_contact_name: str
    emergency_contact_number: str
    emergency_contact_relationship: str

    class Config:
        orm_mode = True


class PatientUpdate(BaseModel):
    email: EmailStr | None
    name: str | None
    display_id: str | None
    phone_number: str | None
    dob: date | None
    blood_group: str | None
    gender: Gender | None
    marital_status: str | None
    occupation: str | None
    insurance_provider: str | None
    address: str | None
    emergency_contact_name: str | None
    emergency_contact_number: str | None
    emergency_contact_relationship: str | None

    class Config:
        orm_mode = True