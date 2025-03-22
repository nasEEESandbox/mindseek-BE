from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import date
from app.db.session import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    status = Column(Enum("confirmed", "waiting"), nullable="False")
    purpose_of_visit = Column(String, nullable=False)
    planned_assessment = Column(String, nullable=True)
    session_summary = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))

    psychiatrist = relationship("Psychiatrist", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")
    diagnoses = relationship("Diagnosis", back_populates="appointments")