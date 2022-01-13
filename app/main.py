from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.teacher import Teacher
from models.student import Student
from models.pet import Pet

if __name__ == "__main__":
    # Create tables from base
    DB_URI = 'postgresql://user:passwd@database/school'
    engine = create_engine(DB_URI, echo=True)
    Base.metadata.create_all(engine, checkfirst=True)

    # Create a session for CRUD
    with sessionmaker(bind=engine)() as session:
        # Delete/Reset
        session.query(Pet).delete()
        session.query(Student).delete()
        session.query(Teacher).delete()

        # Add
        teachers = [Teacher(0, "John"), Teacher(1, "Mary"), Teacher(2, "Jeff")]
        students = [Student(0, "Kyle", 10, 0), Student(1, "Lisa", 9, 0), Student(2, "Elise", 10, 0), Student(3, "Grace", 10, 1)]
        pets = [Pet(0, "Rosco", 0), Pet(1, "Spot", 0), Pet(2, "Shadow", 2)]
        [session.add(t) for t in teachers]
        [session.add(s) for s in students]
        [session.add(p) for p in pets]
        session.commit()

        # Query
        teacher_john = session.query(Teacher).filter_by(name="John").first()
        johns_students = teacher_john = teacher_john.students
        print([s.name for s in johns_students])
        # ['Kyle', 'Lisa', 'Elise']

        johns_pets = sum([s.pet for s in johns_students if s.pet], [])  # flatten for many-one
        print([p.nickname for p in johns_pets])
        # ['Rosco', 'Spot', 'Shadow']
