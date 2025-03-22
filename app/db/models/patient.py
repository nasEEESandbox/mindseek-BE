from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from app.db.session import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String, nullable=True)
    dob = Column(Date, nullable=True)
    psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))

    user = relationship("User", back_populates="patient")
    psychiatrist = relationship("Psychiatrist", back_populates="patients")
    appointments = relationship("Appointment", back_populates="patient")
    medications = relationship("Medication", back_populates="patient")