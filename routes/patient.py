from flask import Blueprint, jsonify, render_template, session, redirect
from models.patient import get_patient, get_public_patient

patient_bp = Blueprint("patient", __name__, url_prefix="/api/v1/patient")


# ---------------------------------------------------------
# PRIVATE VIEW — FULL DETAILS (doctor/admin only)
# ---------------------------------------------------------
@patient_bp.route("/<qr_id>", methods=["GET"])
def private_view(qr_id):

    # CHECK AUTH
    logged_in = session.get("logged_in", False)
    role = session.get("role", None)

    # not logged in
    if not logged_in:
        return redirect(f"/api/v1/auth/login?next=/api/v1/patient/{qr_id}")

    # not clinician
    if role not in ("doctor", "admin"):
        return "Access denied — only medical staff allowed", 403

    # retrieve full data
    patient = get_patient(qr_id)

    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    return render_template("patient.html", patient=patient, authorized=True)


# ---------------------------------------------------------
# PUBLIC EMERGENCY VIEW — NO login required
# ---------------------------------------------------------
@patient_bp.route("/public/<qr_id>", methods=["GET"])
def public_view(qr_id):

    # IMPORTANT: public permissions
    session["logged_in"] = False  
    session["role"] = None        

    patient = get_public_patient(qr_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    return render_template("patient.html", patient=patient, authorized=False)

