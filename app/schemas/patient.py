from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List

class PatientResponse(BaseModel):
    id: int
    display_id: str
    email: EmailStr
    government_id: str
    name: str
    dob: date
    phone_number: str
    blood_group: str
    marital_status: str
    occupation: str
    insurance_provider: str
    address: str
    emergency_contact_name: str
    emergency_contact_number: str
    emergency_contact_relationship: str
    psychiatrist_id: int
    appointment_ids: List[int]
    latest_diagnosis_id: int
    latest_medication_id: int
    photo_url: str

    class Config:
        from_attributes = True


class PatientCreate(BaseModel):
    email: EmailStr
    display_id: str
    government_id: str
    name: str
    dob: date
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
    phone_number: str | None
    dob: date | None
    blood_group: str | None
    marital_status: str | None
    occupation: str | None
    insurance_provider: str | None
    address: str | None
    emergency_contact_name: str | None
    emergency_contact_number: str | None
    emergency_contact_relationship: str | None

    class Config:
        orm_mode = True