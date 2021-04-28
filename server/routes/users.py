from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from server.auth.auth_handler import sing_in

from server.collections.users import (
    add_new_user,
    verify_password,
    retrieve_user_by_email
)

from server.schemas.users import (
    UserLoginSchema,
    UserSchema,
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()


@router.post("/singup", description="Cadastrar usuário na base de dados", name="Cadastrar usuário")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    user_db = await retrieve_user_by_email(user["email"])
    if user_db:
        raise HTTPException(status_code=400, detail=ErrorResponseModel(user, 400, "Dados já existentes na base"))
    new_user = await add_new_user(user)
    return ResponseModel(new_user, "Usuário criado com sucesso")

@router.post("/login", description="Obter Token de acesso", name="Obter AccessToken")
async def user_login(user: UserLoginSchema = Body(...)):
    user = jsonable_encoder(user)
    user_db = await retrieve_user_by_email(user["email"])
    if user_db:
        password_db = user_db["password"]
        if verify_password(user["password"], password_db):
            return sing_in(user_db["email"])
    raise HTTPException(status_code=404, detail=ErrorResponseModel(user, 404, "Usuário não encontrado/Credenciais inválidas"))
