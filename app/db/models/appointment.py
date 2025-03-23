from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.utils.constant import AppointmentStatus


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, unique=True)
    datetime = Column(DateTime, nullable=True)
    status = Column(Enum(AppointmentStatus), nullable=True)
    purpose_of_visit = Column(String, nullable=True)
    planned_assessment = Column(String, nullable=True)
    session_summary = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))

    psychiatrist = relationship("Psychiatrist", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")
    diagnoses = relationship("Diagnosis", back_populates="appointments")