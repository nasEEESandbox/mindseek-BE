from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from app.db.session import Base

class Psychiatrist(Base):
    __tablename__ = "psychiatrists"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    government_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=True)
    phone_number = Column(String, nullable=False)
    license_number = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    consultation_fee = Column(String, nullable=False)

    user = relationship("User", back_populates="psychiatrist")
    patients = relationship("Patient", back_populates="psychiatrist")
    appointments = relationship("Appointment", back_populates="psychiatrist")

    @hybrid_property
    def age(self):
        if self.dob is None:
            return None
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))