MedQR — Smart Medical QR System

MedQR is a secure web application that allows doctors/admins to access full patient medical records and provides public emergency access to essential patient information via QR codes. It integrates MongoDB for data storage, Flask for the backend, and QR codes for easy patient identification.

How it Works

Doctors/Admins log in to view full patient records, prescriptions, and visits.

Public users can scan a patient’s QR code to see essential info (blood group, allergies, emergency contacts).

QR codes are generated automatically for each patient and link to their public page.

Passwords are securely hashed, and session management ensures data privacy.

How to Run
Install dependencies:

pip install -r requirements.txt


Create a .env file with your MongoDB URI and secret keys.

Start the server:

python app.py


Access the app at http://localhost:5000.
