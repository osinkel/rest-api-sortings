from pymongo import MongoClient
from src.config import settings

client = MongoClient(settings.DB_HOST, settings.DB_PORT, connect=False)

db = client[settings.DB_NAME]

collection = db['sorting']
