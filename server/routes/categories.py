from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from typing import Optional

from server.collections.categories import (
    add_new_category,
    update_category,
    retrieve_all_categories,
    retrieve_category_by_name,
    retrieve_active_categories
)

from server.schemas.categories import (
    CategorySchema,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()

@router.post("/category", description="Cadastrar uma categoria na base de dados", name="Cadastrar categoria")
async def add_update_category(category: CategorySchema = Body(...)):
    new_data = jsonable_encoder(category)
    category_db = await retrieve_category_by_name(new_data["category"])
    if category_db:
        updated_category = await update_category(new_data)
        if updated_category:
            return ResponseModel(updated_category, "Categoria atualizada com sucesso")
        raise HTTPException(status_code=400, detail="Erro ao atualizar categoria")
    new_category = await add_new_category(new_data)
    return ResponseModel(new_category, "Categoria cadastrada com sucesso")

@router.get("/categories", description="Consultar categorias", name="Consultar categorias")
async def get_categories(active_categories: Optional[bool] = None):
    if active_categories is not None and active_categories != False:
        categories = await retrieve_active_categories()
        return ResponseModel(categories, "Categorias retornada com sucesso")
    categories = await retrieve_all_categories()
    return ResponseModel(categories, "Categorias retornada com sucesso")
