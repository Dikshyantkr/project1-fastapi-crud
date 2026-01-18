
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# --------------------
# USER MODEL & STORAGE
# --------------------

class User(BaseModel):
    name: str
    contact: str
    role: str

users = []
current_user_id = 1


@app.post("/users")
def create_user(user: User):
    global current_user_id
    user_data = {
        "id": current_user_id,
        "name": user.name,
        "contact": user.contact,
        "role": user.role
    }
    users.append(user_data)
    current_user_id += 1
    return {"message": "User created", "user": user_data}


@app.get("/users")
def get_users():
    return users


# -------------------------
# ATTENDANCE MODEL & STORE
# -------------------------

attendance_records = []
current_attendance_id = 1


# CHECK-IN
@app.post("/attendance/check-in/{user_id}")
def check_in(user_id: int):
    global current_attendance_id

    # Validate user
    user_exists = any(user["id"] == user_id for user in users)
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if already checked in
    for record in attendance_records:
        if record["user_id"] == user_id and record["status"] == "checked_in":
            raise HTTPException(status_code=400, detail="User already checked in")

    record = {
        "id": current_attendance_id,
        "user_id": user_id,
        "check_in_time": datetime.now(),
        "check_out_time": None,
        "status": "checked_in"
    }

    attendance_records.append(record)
    current_attendance_id += 1

    return {"message": "Check-in successful", "attendance": record}


# CHECK-OUT
@app.post("/attendance/check-out/{user_id}")
def check_out(user_id: int):
    for record in attendance_records:
        if record["user_id"] == user_id and record["status"] == "checked_in":
            record["check_out_time"] = datetime.now()
            record["status"] = "checked_out"
            return {"message": "Check-out successful", "attendance": record}

    raise HTTPException(status_code=400, detail="User is not checked in")


# VIEW ALL ATTENDANCE
@app.get("/attendance")
def get_attendance():
    return attendance_records


# VIEW ATTENDANCE BY USER
@app.get("/attendance/{user_id}")
def get_user_attendance(user_id: int):
    user_records = [r for r in attendance_records if r["user_id"] == user_id]
    if not user_records:
        raise HTTPException(status_code=404, detail="No attendance records found")
    return user_records

