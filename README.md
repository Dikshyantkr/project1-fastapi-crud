# FastAPI CRUD Backend – Powerbank Borrowing System

This project is a **FastAPI-based CRUD backend application** built as part of my internship learning phase.  
The goal is to understand and implement **core backend concepts** using a simple, real-world use case.

---

## 📌 Project Idea

The application simulates a **powerbank (resource) borrowing system** for offices or colleges.

It allows:
- Creating users (students / staff)
- Viewing all users
- Fetching a user by ID
- Updating user details
- Deleting users
- (Upcoming) Resource borrowing & return logic

This project focuses on **CRUD fundamentals before moving to databases and authentication**.

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **Testing Tool:** curl (CLI-based API testing)  
- **Platform:** Linux (Ubuntu / WSL)  

---

## 🚀 Features Implemented (Current Progress)

### User APIs (Full CRUD)
- `POST /users` → Create a user  
- `GET /users` → List all users  
- `GET /users/{id}` → Fetch user by ID  
- `PUT /users/{id}` → Update user details  
- `DELETE /users/{id}` → Delete user  

Data is currently stored **in-memory** (Python list) for learning purposes.

---

## 🧪 API Testing

All APIs are tested using `curl` from the terminal.

Example:
```bash
curl -X POST http://127.0.0.1:8000/users \
-H "Content-Type: application/json" \
-d '{"name":"Aman","contact":"aman@college.edu","role":"student"}'
