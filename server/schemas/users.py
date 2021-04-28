from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "email": "admin@example.com",
                "password": "password"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "email": "admin@example.com",
                "password": "password"
            }
        }
        

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }
    

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
