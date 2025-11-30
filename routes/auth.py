from flask import Blueprint, request, render_template, redirect, session, url_for
from models.user import users_col
import bcrypt

print("AUTH BLUEPRINT FILE EXECUTED")

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


# --------------------
# SHOW LOGIN PAGE
# --------------------
@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


# --------------------
# PROCESS LOGIN FORM
# --------------------
@auth_bp.route("/login", methods=["POST"])
def login_submit():
    email = request.form.get("email")
    password = request.form.get("password").encode()
    next_url = request.form.get("next_url")   # <-- IMPORTANT

    print("\n=== LOGIN ATTEMPT ===")
    print("Email entered:", email)
    print("Submitted next_url:", next_url)

    user = users_col.find_one({"email": email})
    print("USER FOUND:", user)

    if not user:
        return "Invalid email or password", 401

    stored_hash = user["passwordHash"]

    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode()

    password_ok = bcrypt.checkpw(password, stored_hash)
    print("Bcrypt check:", password_ok)

    if password_ok:
        session["logged_in"] = True
        session["role"] = user["role"]
        session["email"] = user["email"]
        session["name"] = user["name"]

        print("LOGIN SUCCESS!")

        # redirect properly
        if next_url:
            return redirect(next_url)

        return redirect("/")

    return "Invalid credentials", 401


@auth_bp.route("/logout")
def logout():
    qr = request.args.get("qr")
    session.clear()

    if qr:
        return redirect(f"/api/v1/patient/public/{qr}")

    return redirect("/")

