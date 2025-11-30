from flask import Flask
from routes.auth import auth_bp
from routes.patient import patient_bp
from config import Config

app = Flask(__name__, template_folder="templates")
app.secret_key = Config.SECRET_KEY

# register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(patient_bp)

print("REGISTERED ROUTES:")
print(app.url_map)

@app.route("/")
def home():
    return "MedQR server running — use /api/v1/patient/public/QRxxx"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
