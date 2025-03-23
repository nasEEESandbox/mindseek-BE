from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

# from app.db.models.medicine import Medicine
# from app.db.models.patient import Patient

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    dosage = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    notes = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    medicines = relationship("Medicine", back_populates="medications")
    patient = relationship("Patient", back_populates="medications")