from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from database import engine, SessionLocal
from models import Base, User, Course, Grade

app = FastAPI()

Base.metadata.create_all(bind=engine)

# --- DATABASE ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- SCHEMAS ---
class UserCreate(BaseModel):
    username: str
    email: str

class CourseCreate(BaseModel):
    name: str
    description: str
    user_id: int

class GradeCreate(BaseModel):
    name: str     # Notun ismi (Vize, Final)
    score: int    # Puan
    course_id: int # Hangi ders?

# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "StudyTracker API is running 🚀"}

# 1. USER
@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# 2. COURSE
@app.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == course.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_course = Course(name=course.name, description=course.description, owner_id=course.user_id)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# 3. GRADE (YENİ 🔥)
@app.post("/grades")
def create_grade(grade: GradeCreate, db: Session = Depends(get_db)):
    # Ders var mı kontrol et
    course = db.query(Course).filter(Course.id == grade.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    new_grade = Grade(name=grade.name, score=grade.score, course_id=grade.course_id)
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    return new_grade

@app.get("/grades")
def get_grades(db: Session = Depends(get_db)):
    return db.query(Grade).all()