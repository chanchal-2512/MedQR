from pymongo import MongoClient
from config import Config
import bcrypt

client = MongoClient(Config.MONGO_URI)
db = client["mediqr"]
users_col = db['users']

def create_user(email, password, name, role):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = {"email": email, "passwordHash": password_hash, "name": name, "role": role}
    users_col.insert_one(user)
