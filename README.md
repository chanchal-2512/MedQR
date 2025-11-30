### MedQR — Smart Medical QR System
MedQR is a secure web application that allows doctors/admins to access full patient medical records and provides public emergency access to essential patient information via QR codes.

### How it Works
- Doctors/Admins log in to view full patient records, prescriptions, and visits.
- Public users can scan a patient’s QR code to see essential info (blood group, allergies, emergency contacts).
- QR codes are generated automatically for each patient and link to their public page.
- Passwords are securely hashed, and session management ensures data privacy.

## How to Run

- **Install dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```

- **Set up environment variables:**  
    Create a `.env` file with your MongoDB URI and secret keys:
    ```env
    MONGODB_URI=your_mongodb_uri_here
    SECRET_KEY=your_flask_secret_here
    JWT_SECRET_KEY=your_jwt_secret_here
    ```

- **Start the server:**  
    ```bash
    python app.py
    ```

- **Access the app:**  
    Open in your browser: `http://localhost:5000`
