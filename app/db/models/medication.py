from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import date
from app.db.session import Base

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    dosage = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    notes = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    medicines = relationship("Medicine", back_populates="medications")
    patient = relationship("Patient", back_populates="medications")