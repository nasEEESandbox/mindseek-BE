from sqlalchemy import Column, Integer, String, Enum
from app.db.session import Base
from sqlalchemy.orm import relationship

from app.utils.constant import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    nip = Column(String, unique=True, index=True, nullable=True)
    role = Column(Enum(UserRole), nullable=False)

    admin = relationship("Admin", back_populates="user", uselist=False)
    psychiatrist = relationship("Psychiatrist", back_populates="user", uselist=False)
