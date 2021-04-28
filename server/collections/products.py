from server.database import get_collection
from bson import ObjectId

product_collection = get_collection('docesWebApi', 'products')

# Helpers

def product_helper(product) -> dict:
    return {
        "product_name": product["product_name"],
        "description": product["description"],
        "value": product["value"],
        "image": product["image"],
        "active": product["active"],
        "category": product["category_id"],
    }

# CRUD methods
async def add_new_product(product_data: dict) -> dict:
    new_data = {
        "product_name": product_data["product_name"],
        "description": product_data["description"],
        "value": product_data["value"],
        "image": product_data["image"],
        "active": product_data["active"],
        "category_id": product_data["category_id"],
    }
    product = await product_collection.insert_one(new_data)
    new_product = await product_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_data)
    
async def retrieve_all_products() -> list:
    list_products = []
    async for product in product_collection.find():
        list_products.append(product_helper(product))
    return list_products

async def retrieve_active_products() -> list:
    list_products = []
    async for product in product_collection.find({"active": True}):
        list_products.append(product_helper(product))
    return list_products

async def retrieve_products_by_category(category: int) -> list:
    list_products = []
    async for product in product_collection.find({"category": category}):
        list_products.append(product_helper(product))
    return list_products

async def retrieve_product_by_name(product_name: str) -> dict:
    product = await product_collection.find_one({"product_name": product_name})
    if product:
        return product_helper(product)
    return None

async def update_product(product: dict) -> dict:
    try:
        await product_collection.replace_one({"product_name": product["product_name"]}, product)
        new_product = await product_collection.find_one({"product_name": product["product_name"]})
        return product_helper(new_product)
    except Exception as error:
        print(error)
        return None
