
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("FileUpload", back_populates="owner")


class FileUpload(Base):
    __tablename__ = "Uploadsfiles12"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    message = Column(String, index=True)
    link = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    #
    # owner = relationship("User", back_populates="items")
