from fastapi import APIRouter, Body, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from typing import Optional

from server.auth.auth_bearer import JWTBearer

from server.collections.images import (
    add_new_image,
    get_image_by_name,
    get_image_by_name_and_image,
    get_all_images_in_page
)

from server.schemas.images import (
    ImageSchema,
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

# HTTP Requests
@router.get("/images/{page}", description="Retorna imagens da página", name="Imagens Página", dependencies=[Depends(JWTBearer())])
async def get_all_images_page(page: str):
    images = await get_all_images_in_page(page)
    if images:
        return ResponseModel(images, "Dados retornados com sucesso")
    raise HTTPException(status_code=404, detail="Dados não encontrados")


@router.get("/images/{page}/{name}", description="Retorna informações da imagem", name="Informações Imagens", dependencies=[Depends(JWTBearer())])
async def get_image_data(page: str,
                         name: str,
                         image: Optional[str] = None):
    if image is None or image == "":
        response = await get_image_by_name(page, name)
        if response:
            return ResponseModel(response, "Dados retornados com sucesso")
        raise HTTPException(status_code=404, detail="Dados não encontrados")
    raise HTTPException(status_code=404, detail="Dados não encontrados")

@router.post("/images", description="Cadastro de imagem", name="Cadastrar imagem", dependencies=[Depends(JWTBearer())])
async def save_new_image(image: ImageSchema = Body(...)):
    image = jsonable_encoder(image)
    new_image = await add_new_image(image)
    if new_image:
        return ResponseModel(new_image, "Imagem adicionada com sucesso")
    raise HTTPException(status_code=400, detail="Erro ao salvar dados")
    