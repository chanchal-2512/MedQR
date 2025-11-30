from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client["mediqr"]
patients_col = db["patients"]
users_col = db["users"]

# Full private doctor/admin view
def get_patient(qr_id):
    return patients_col.find_one({"qrId": qr_id}, {"_id": 0})


# Public emergency view — ONLY essential info
def get_public_patient(qr_id):
    patient = patients_col.find_one({"qrId": qr_id})
    if not patient:
        return None

    return {
        "qrId": patient.get("qrId"),
        "name": patient.get("name"),
        "gender": patient.get("gender"),
        "bloodGroup": patient.get("bloodGroup"),
        "allergies": patient.get("allergies"),
        "insurance": patient.get("insurance"),
        "contacts": patient.get("contacts")
    }
