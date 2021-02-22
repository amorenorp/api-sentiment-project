import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.shout_park

coll_character = db.characters
coll_dialogue = db.dialogues

