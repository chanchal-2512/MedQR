import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MongoDB URI (use local default if not set in environment)
    MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/medqr")

    # Flask secret key
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")

    # JWT configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_dev_secret")
    JWT_ALGORITHM = "HS256"
