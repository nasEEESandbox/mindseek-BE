from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.db.session import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    display_id = Column(String, unique=True, nullable=True)
    government_id = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    name = Column(String, nullable=True)
    dob = Column(Date, nullable=True)
    phone_number = Column(String, nullable=True)
    blood_group = Column(String, nullable=True)
    marital_status = Column(String, nullable=True)
    occupation = Column(String, nullable=True)
    insurance_provider = Column(String, nullable=True)
    address = Column(String, nullable=True)
    emergency_contact_name = Column(String, nullable=True)
    emergency_contact_number = Column(String, nullable=True)
    emergency_contact_relationship = Column(String, nullable=True)
    psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))

    psychiatrist = relationship("Psychiatrist", back_populates="patients")
    appointments = relationship("Appointment", back_populates="patient")
    medications = relationship("Medication", back_populates="patient")
    diagnoses = relationship("Diagnosis", back_populates="patients")

    @hybrid_property
    def appointment_ids(self):
        return [appointment.id for appointment in self.appointments]
    
    @hybrid_property
    def latest_diagnosis_id(self):
        latest_diagnosis = max(self.diagnoses, key=lambda d: d.diagnosed_date, default=None)
        return latest_diagnosis.id if latest_diagnosis else None
    
    @hybrid_property
    def latest_medication_id(self):
        latest_medication = max(self.medications, key=lambda m: m.start_date, default=None)
        return latest_medication.id if latest_medication else None

    @hybrid_property
    def photo_url(self):
        return f"https://ui-avatars.com/api/?name={self.name}&background=random&rounded=true&bold=true"