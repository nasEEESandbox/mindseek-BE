import enum

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import date
from app.db.session import Base

class Severity(enum.Enum):
    SEVERE = "SEVERE"
    NORMAL = "NORMAL"
    EASY = "EASY"

class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    diagnosed_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=True)
    severity = Column(Enum(Severity), nullable=False)

    appointments = relationship("Appointment", back_populates="diagnoses")
    patients = relationship("Patient", back_populates="diagnoses")