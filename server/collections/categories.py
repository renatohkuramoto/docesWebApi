from server.database import get_collection
from bson import ObjectId

category_collection = get_collection('docesWebApi', 'category')

# Helpers

def category_helper(category: dict) -> dict:
    return {
        "category_id": category["category_id"],
        "category": category["category"],
        "active": category["active"]
    }
    

# CRUD methods
async def add_new_category(category_data: dict) -> dict:
    totals = 0
    async for element in category_collection.find():
        totals += 1

    new_data = {
        "category_id": totals + 1,
        "category": category_data["category"],
        "active": category_data["active"]
    }

    category = await category_collection.insert_one(new_data)
    new_category = await category_collection.find_one({"_id": category.inserted_id})
    return category_helper(new_category)

async def update_category(category: dict) -> dict:
    try:
        await category_collection.update_one({"category": category["category"]}, {"$set": category})
        new_category = await category_collection.find_one({"category": category["category"]})
        return category_helper(new_category)
    except Exception as error:
        print(error)
        return None

async def retrieve_all_categories() -> list:
    list_categories = []
    async for category in category_collection.find():
        list_categories.append(category_helper(category))
    return list_categories

async def retrieve_category_by_name(category_name: str) -> dict:
    category = await category_collection.find_one({"category": category_name})
    if category:
        return category_helper(category)
    return None

async def retrieve_active_categories() -> list:
    list_categories = []
    async for category in category_collection.find({"active": True}):
        list_categories.append(category_helper(category))
    return list_categories
