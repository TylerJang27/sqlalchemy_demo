from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key = True)
    nickname = Column(String(50), nullable=True)

    student_id = Column(Integer, ForeignKey('student.id'), nullable=True)

    # Relationships
    student = relationship("Student", back_populates="pet")

        
    def __init__(self, id, nickname, s_id):
        self.id = id
        self.nickname = nickname
        self.student_id = s_id