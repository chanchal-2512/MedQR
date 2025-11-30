import qrcode
import socket
from pymongo import MongoClient

# --- Get LAN IP of your laptop ---
def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP

lan_ip = "192.168.1.215"
print("LAN IP =", lan_ip)

# --- Connect MongoDB ---
client = MongoClient("mongodb://localhost:27017")
db = client["mediqr"]
patients = db["patients"]

# --- Loop through each patient ---
for p in patients.find():
    qrId = p["qrId"]
    url = f"http://{lan_ip}:5000/api/v1/patient/public/{qrId}"
    img = qrcode.make(url)
    filename = f"QR_{qrId}.png"
    img.save(filename)
    print("Generated:", filename, "->", url)
