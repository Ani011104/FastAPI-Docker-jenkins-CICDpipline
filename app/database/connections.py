from pymongo import MongoClient


MONGO_URI = "mongodb://admin:admin@mongo:27017"
# @mongo here refers to docker container name and not the image or the local host name 

client = MongoClient(MONGO_URI)
db = client["task_db"]
collection =db['tasks']

