from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable=False)

    # Relationships
    students = relationship("Student", back_populates="teacher")


    def __init__(self, id, name):
        self.id = id
        self.name = name