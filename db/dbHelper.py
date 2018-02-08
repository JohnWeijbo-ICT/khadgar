import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['test']

cursor = db.test.find()

for document in cursor:
    print(document)
