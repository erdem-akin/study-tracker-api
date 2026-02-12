from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    
    courses = relationship("Course", back_populates="owner")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="courses")
    grades = relationship("Grade", back_populates="course") # Dersin notları olacak

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Örn: Vize 1, Final
    score = Column(Integer)            # Örn: 85
    course_id = Column(Integer, ForeignKey("courses.id")) # Hangi derse ait?

    course = relationship("Course", back_populates="grades")