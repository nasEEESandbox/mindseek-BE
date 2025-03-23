from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from app.db.session import Base

class Psychiatrist(Base):
    __tablename__ = "psychiatrists"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    display_id = Column(String, nullable=True)
    government_id = Column(String, nullable=True)
    name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    dob = Column(Date, nullable=True)
    phone_number = Column(String, nullable=True)
    license_number = Column(String, nullable=True)
    specialization = Column(String, nullable=True)
    consultation_fee = Column(String, nullable=True)

    availability = relationship("PsychiatristAvailability", back_populates="psychiatrist")
    user = relationship("User", back_populates="psychiatrist")
    patients = relationship("Patient", back_populates="psychiatrist")
    appointments = relationship("Appointment", back_populates="psychiatrist")

    @hybrid_property
    def age(self):
        if self.dob is None:
            return None
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    @hybrid_property
    def photo_url(self):
        return f"https://ui-avatars.com/api/?name={self.name}&background=random&rounded=true&bold=true"