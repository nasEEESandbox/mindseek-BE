from sqlalchemy import Column, Integer, ForeignKey, Enum, Time
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.utils.constant import Weekday


class PsychiatristAvailability(Base):
    __tablename__ = "psychiatrist_availabilities"

    id = Column(Integer, primary_key=True)
    psychiatrist_id = Column(Integer, ForeignKey("psychiatrists.id"))
    day_of_week = Column(Enum(Weekday), nullable=True)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)

    psychiatrist = relationship("Psychiatrist", back_populates="availability")