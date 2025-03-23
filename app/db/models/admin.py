from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.db.session import Base
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String, nullable=True)

    user = relationship("User", back_populates="admin")
