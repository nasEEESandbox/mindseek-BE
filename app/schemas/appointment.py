from pydantic import BaseModel
from datetime import datetime
from app.utils.constant import AppointmentStatus

class AppointmentResponse(BaseModel):
    id: int | None
    datetime: datetime | None
    status: AppointmentStatus | None
    purpose_of_visit: str | None
    planned_assessment: str | None
    session_summary: str | None
    patient_id: int | None
    psychiatrist_id: int | None


class AppointmentCreate(BaseModel):
    datetime: datetime
    status: AppointmentStatus
    purpose_of_visit: str
    planned_assessment: str
    session_summary: str
    patient_id: int
    psychiatrist_id: int


class AppointmentUpdate(BaseModel):
    appointment_id: int | None
    datetime: datetime | None
    status: AppointmentStatus | None
    purpose_of_visit: str | None
    planned_assessment: str | None
    session_summary: str | None
    patient_id: int | None
    psychiatrist_id: int | None


# class Appointment(Base):
#     __tablename__ = "appointments"
#
#     id = Column(Integer, primary_key=True, unique=True)
#     datetime = Column(DateTime, nullable=True)
#     status = Column(Enum(AppointmentStatus), nullable=True)
#     purpose_of_visit = Column(String, nullable=True)
#     planned_assessment = Column(String, nullable=True)
#     session_summary = Column(String, nullable=True)
#     patient_id = Column(Integer, ForeignKey("patients.id"))
#     psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))
#
#     psychiatrist = relationship("Psychiatrist", back_populates="appointments")
#     patient = relationship("Patient", back_populates="appointments")
#     diagnoses = relationship("Diagnosis", back_populates="appointments")