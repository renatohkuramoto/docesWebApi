from fastapi import FastAPI
from server.routes.users import router as UserRouter
from server.routes.images import router as ImageRouter
from server.routes.products import router as ProductRouter
from server.routes.categories import router as CategoryRouter

# Tags Swagger
tags_metadata = [
    {
        "name": "Users",
        "description": "Endpoint para cadastrar ou efeturar login"
    },
    {
        "name": "Images",
        "description": "Endpoint para cadastro e consulta de imagens"
    },
    {
        "name": "Products",
        "description": "Endpoint para cadastro e consulta de produtos"
    },
    {
        "name": "Categories",
        "description": "Endpoint para cadastro e consulta de categorias"
    }
]

app = FastAPI(
    title="API webDoces",
    description="Backend do website webDoces",
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.include_router(UserRouter, tags=["Users"], prefix="/api")
app.include_router(ImageRouter, tags=["Images"], prefix="/api")
app.include_router(ProductRouter, tags=["Products"], prefix="/api")
app.include_router(CategoryRouter, tags=["Categories"], prefix="/api")