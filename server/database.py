import motor.motor_asyncio

def get_collection(database, collection):
    MONGO_URL = "mongodb+srv://admin:password@cluster0.xfmcv.mongodb.net/{}?retryWrites=true&w=majority".format(database)
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
    database = client[database]
    return database.get_collection("{}_collection".format(collection))
