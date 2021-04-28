from typing import Optional
from pydantic import BaseModel, Field


class ImageSchema(BaseModel):
    page: str = Field(...)
    name: str = Field(...)
    image: str = Field(...)
    path: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "page": "home",
                "name": "background",
                "image": "background1.png",
                "path": "C:/images/"
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
