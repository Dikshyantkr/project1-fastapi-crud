# FastAPI CRUD Backend – Attendance Management System

This project is a **FastAPI-based backend application** built as part of my internship learning phase.  
The goal is to understand and implement **core backend concepts** using a real-world use case.

---

## 📌 Project Idea

The application simulates a **basic attendance management system** for offices or colleges.

It allows:
- Managing users (employees / students)
- Logging check-in and check-out times
- Preventing duplicate check-ins
- Viewing attendance history

This project focuses on **CRUD fundamentals, REST APIs, and backend logic** before moving to databases and authentication.

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **Testing Tool:** curl (CLI-based API testing)  
- **Platform:** Linux (Ubuntu / WSL)  

---

## 🚀 Features Implemented

### 👤 User Management APIs
- `POST /users` → Create a user  
- `GET /users` → List all users  
- `GET /users/{id}` → Fetch user by ID  
- `PUT /users/{id}` → Update user details  
- `DELETE /users/{id}` → Delete user  

---

### ⏱ Attendance APIs
- `POST /attendance/check-in/{user_id}` → Check-in a user  
- `POST /attendance/check-out/{user_id}` → Check-out a user  
- `GET /attendance` → View all attendance records  

### Attendance Rules
- A user **cannot check-in twice** without checking out
- Check-in & check-out timestamps are recorded
- Status is tracked (`checked_in`, `checked_out`)

---

## 🧪 API Testing

All APIs are tested using `curl` from the terminal.

### Example: Create User
```bash
curl -X POST http://127.0.0.1:8000/users \
-H "Content-Type: application/json" \
-d '{"name":"Aman","contact":"aman@office.com","role":"employee"}'
```

### Example: Check-in
```bash
curl -X POST http://127.0.0.1:8000/attendance/check-in/1
```

### Example: View Attendance
```bash
curl http://127.0.0.1:8000/attendance
```

---

## ▶️ How to Run the Project

```bash
# Activate virtual environment
source venv/bin/activate

# Run the FastAPI server
uvicorn app.main:app --reload
```

Server runs at:
```
http://127.0.0.1:8000
```

Swagger Docs:
```
http://127.0.0.1:8000/docs
```

---

## 🔜 Next Steps

- Database integration (PostgreSQL)
- Authentication & authorization
- Attendance reports (daily / user-based)
- Deployment

---

## 📚 Learning Outcomes

- REST API design
- FastAPI request/response handling
- HTTP methods & status codes
- Backend business logic
- API testing via CLI tools
- Git & GitHub workflow

---

## 👤 Author
**Dikshyant Kumar Routray**  
Backend Intern

