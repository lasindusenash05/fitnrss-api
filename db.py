from motor.motor_asyncio import AsyncIOMotorClient

client = None
db = None

async def connect_db():
    global client, db
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.fitness