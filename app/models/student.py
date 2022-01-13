from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=True)

    # Relationships
    teacher = relationship("Teacher", back_populates="students")
    pet = relationship("Pet", back_populates="student")


    def __init__(self, id, name, age, t_id):
        self.id = id
        self.name = name
        self.age = age
        self.teacher_id = t_id