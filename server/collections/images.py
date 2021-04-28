from server.database import get_collection
from typing import Optional
import bson

image_collection = get_collection('docesWebApi', 'images')

# Helpers
def images_helper(image) -> dict:
    return {
        "page": image["page"],
        "name": image["name"],
        "image": image["image"],
        "path": image["path"],
    }

def encode_utf(string: str) -> str:
    return string.encode()

# CRUD

async def add_new_image(image_data: dict) -> dict:
    new_data = {
        "page": image_data["page"],
        "name": image_data["name"],
        "image": image_data["image"],
        "path": image_data["path"],
    }
    image = await image_collection.insert_one(new_data)
    new_image = await image_collection.find_one({"_id": image.inserted_id})
    if new_image:
        return images_helper(new_image)
    return None

async def get_all_images_in_page(page: str) -> list:
    list_images = []
    async for image in image_collection.find({"page": page}):
        list_images.append(images_helper(image))
    return list_images

async def get_image_by_name(page: str, name: str) -> dict:
    page = encode_utf(page)
    name = encode_utf(name)
    image = await image_collection.find_one({"page": page, "name": name})
    if image:
        return images_helper(image)
    return None

async def get_image_by_name_and_image(page: str, name: str, image:str) -> dict:
    page = encode_utf(page)
    name = encode_utf(name)
    image = encode_utf(image)
    image = await image_collection.find_one({"page": page , "name": name, "image": image})
    if image:
        return images_helper(image)
    return None
