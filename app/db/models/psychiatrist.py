from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from app.db.session import Base
import enum

class Weekday(enum.Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"

class PsychiatristAvailability(Base):
    __tablename__ = "psychiatrist_availabilities"

    id = Column(Integer, primary_key=True)
    psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))
    day_of_week = Column(Enum(Weekday), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    psychiatrist = relationship("Psychiatrist", back_populates="availability")

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