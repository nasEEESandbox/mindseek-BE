from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import date
from app.db.session import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True)
    medicine_name = Column(String, nullable=False)

    medications = relationship("Medication", back_populates="medicines")