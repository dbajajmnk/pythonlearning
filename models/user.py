from utils.db import db
from bson import ObjectId

class User:
    def __init__(self, name, email, image, phone):
        self.name = name
        self.email = email
        self.image = image
        self.phone = phone

    @staticmethod
    def create(data):
        return db.users.insert_one(data)

    @staticmethod
    def get_all():
        return list(db.users.find())

    @staticmethod
    def update(user_id, data):
        return db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete(user_id):
        return db.users.delete_one({"_id": ObjectId(user_id)})
