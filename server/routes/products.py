from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import Optional

from server.collections.products import (
    add_new_product,
    retrieve_active_products,
    retrieve_all_products,
    retrieve_products_by_category,
    retrieve_product_by_name,
    update_product
)

from server.schemas.products import (
    ProductSchema,
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post("/product", description="Cadastrar um produto na base de dados", name="Cadastrar produto")
async def add_product(product: ProductSchema = Body(...)):
    new_data = jsonable_encoder(product)
    product_db = await retrieve_product_by_name(new_data["product_name"])
    if product_db:
        updated_product = await update_product(new_data)
        if updated_product:
            return ResponseModel(updated_product, "Produto atualizado com sucesso")
        raise HTTPException(status_code=400, detail="Erro ao atualizar produto")
    new_product = await add_new_product(new_data)
    return ResponseModel(new_product, "Produto cadastrado com sucesso")

@router.get("/products", description="Consultar todos os produtos", name="Consultar produtos")
async def get_all_products(product_name: Optional[str] = None,
                           active_products: Optional[bool] = None):
    if product_name is not None:
        product = await retrieve_product_by_name(product_name)
        if product:
            return ResponseModel(product, "Produto retornado com sucesso")
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    elif active_products is not None and active_products != False:
        products = await retrieve_active_products()
        return ResponseModel(products, "Produtos retornados com sucesso")
    products = await retrieve_all_products()
    return ResponseModel(products, "Produtos retornados com sucesso")
