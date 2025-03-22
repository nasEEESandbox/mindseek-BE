from sqlalchemy import Column, Integer, String, Enum
from app.db.session import Base
from sqlalchemy.orm import relationship
import enum

class UserRole(enum.Enum):
    PATIENT = "PATIENT"
    PSYCHIATRIST = "PSYCHIATRIST"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    patient = relationship("Patient", back_populates="user", uselist=False)
    psychiatrist = relationship("Psychiatrist", back_populates="user", uselist=False)
