from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.utils.constant import Severity


class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, unique=True)
    diagnosis_name = Column(String, nullable=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    diagnosed_date = Column(DateTime, nullable=True)
    status = Column(String, nullable=True)
    severity = Column(Enum(Severity), nullable=True)

    appointments = relationship("Appointment", back_populates="diagnoses")
    patients = relationship("Patient", back_populates="diagnoses")