# 📚 StudyTracker API

A robust RESTful API built with **FastAPI** to help students track their courses and grades.
This project demonstrates backend development skills including database relationships, CRUD operations, and clean architecture.

## 🚀 Tech Stack
* **Language:** Python 3.14
* **Framework:** FastAPI
* **Database:** SQLite & SQLAlchemy (ORM)
* **Validation:** Pydantic Schemas

## ⚡ Features
* ✅ **User Management:** Register new students.
* ✅ **Course Tracking:** Add courses to specific users.
* ✅ **Grade System:** Log exam scores for each course.
* ✅ **Clean Architecture:** Separated models, database connection, and API logic.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/erdem-akin/study-tracker-api.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
    ```
4. Open Swagger UI: Go to http://127.0.0.1:8000/docs to test the endpoints.
   Developed by Erdem Akın as a study management backend solution.
