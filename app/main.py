from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# User data model
class User(BaseModel):
    name: str
    contact: str
    role: str

# In-memory storage
users = []
current_id = 1

# CREATE user
@app.post("/users")
def create_user(user: User):
    global current_id
    user_dict = user.dict()
    user_dict["id"] = current_id
    current_id += 1
    users.append(user_dict)
    return {
        "message": "User created successfully",
        "user": user_dict
    }

# READ all users
@app.get("/users")
def get_users():
    return {
        "count": len(users),
        "users": users
    }

# READ user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["contact"] = updated_user.contact
            user["role"] = updated_user.role
            return {
                "message": "User updated successfully",
                "user": user
            }
    raise HTTPException(status_code=404, detail="User not found")

# DELETE user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)
            return {
                "message": "User deleted successfully",
                "user": deleted_user
            }
    raise HTTPException(status_code=404, detail="User not found")
