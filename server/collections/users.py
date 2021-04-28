from server.database import get_collection
from bson import ObjectId
import bcrypt


users_collection = get_collection('docesWebApi', 'users')

# Helpers
def user_helper(user) -> dict:
    return  {
        "username": user["username"],
    }
    
def user_helper_login(user) -> dict:
    return {
        "username": user["username"],
        "email": user["email"],
        "password": user["password"],
    }

def encode_utf(string: str) -> str:
    return string.encode("utf-8")

def verify_password(password_send: str, password_db: str) -> bool:
    if bcrypt.checkpw(encode_utf(password_send), password_db):
        return True
    return None

# CRUD
async def add_new_user(user_data: dict) -> dict:
    new_data = {
        "username": user_data["username"],
        "email": user_data["email"],
        "password": bcrypt.hashpw(encode_utf(user_data["password"]), bcrypt.gensalt())
    }
    user = await users_collection.insert_one(new_data)
    new_user = await users_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def retrieve_user_by_email(email: str) -> str:
    user = await users_collection.find_one({"email": email})
    if user:
        return user_helper_login(user)
    return None
