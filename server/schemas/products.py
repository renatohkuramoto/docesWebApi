from typing import Optional
from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    product_name: str = Field(...)
    description: str = Field(...)
    value: str = Field(...)
    image: str = Field(...)
    active: bool = Field(...)
    category_id: int = Field(...)
    
    class Config:
        schema_extra = {
            "example" : {
                "product_name": "Bolo Sensação",
                "description": "Recheio de morango com cobertura de chocolate",
                "value": "99,99",
                "image": "sensacao.jpeg",
                "active": 1,
                "category_id": 1
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
