from pydantic import BaseModel
from datetime import date


class MedicationResponse(BaseModel):
    id: int | None
    medicine_id: int | None
    dosage: str | None
    start_date: date | None
    end_date: date | None
    notes: str | None
    patient_id: int | None


class MedicationCreate(BaseModel):
    medicine_id: int
    dosage: str
    start_date: date
    end_date: date
    notes: str
    patient_id: int


class MedicationUpdate(BaseModel):
    medicine_id: int | None
    dosage: str | None
    start_date: date | None
    end_date: date | None
    notes: str | None