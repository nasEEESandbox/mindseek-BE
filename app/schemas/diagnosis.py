from pydantic import BaseModel
from datetime import datetime
from app.utils.constant import Severity

class DiagnosisResponse(BaseModel):
    id: int | None
    diagnosis_name: str | None
    appointment_id: int | None
    patient_id: int | None
    diagnosed_date: datetime | None
    status: str | None
    severity: Severity | None


class DiagnosisCreate(BaseModel):
    diagnosis_name: str
    appointment_id: int
    patient_id: int
    diagnosed_date: datetime
    status: str
    severity: Severity


class DiagnosisUpdate(BaseModel):
    diagnosis_id: int | None
    diagnosis_name: str | None
    appointment_id: int | None
    patient_id: int | None
    diagnosed_date: datetime | None
    status: str | None
    severity: Severity | None

# class Diagnosis(Base):
#     __tablename__ = "diagnoses"
#
#     id = Column(Integer, primary_key=True, unique=True)
#     diagnosis_name = Column(String, nullable=True)
#     appointment_id = Column(Integer, ForeignKey("appointments.id"))
#     patient_id = Column(Integer, ForeignKey("patients.id"))
#     diagnosed_date = Column(DateTime, nullable=True)
#     status = Column(String, nullable=True)
#     severity = Column(Enum(Severity), nullable=True)
#
#     appointments = relationship("Appointment", back_populates="diagnoses")
#     patients = relationship("Patient", back_populates="diagnoses")