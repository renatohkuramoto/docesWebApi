from typing import Optional
from pydantic import BaseModel, Field

class CategorySchema(BaseModel):
    category: str = Field(...)
    active: bool = Field(...)
    
    class Config:
        schema_extra = {
        "example": {
            "category": "Bolos",
            "active": 1
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
