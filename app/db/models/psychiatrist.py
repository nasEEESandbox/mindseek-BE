from sqlalchemy import Column, Integer, String, Date, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from app.db.session import Base
from app.utils.constant import default_photo_url, Gender


class Psychiatrist(Base):
    __tablename__ = "psychiatrists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    nip = Column(String, unique=True, index=True, nullable=True, default='000000-0000')
    display_id = Column(String, nullable=True)
    government_id = Column(String, nullable=True)
    name = Column(String, nullable=True)
    gender = Column(Enum(Gender), nullable=True)
    dob = Column(Date, nullable=True)
    phone_number = Column(String, nullable=True)
    license_number = Column(String, nullable=True)
    specialization = Column(String, nullable=True)
    consultation_fee = Column(String, nullable=True)
    is_admin = Column(Boolean, nullable=True, default=False)

    availability = relationship("PsychiatristAvailability", back_populates="psychiatrist")
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
        return default_photo_url(self.name)