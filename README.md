# MedQR — Smart Medical QR System

MedQR is a web-based application that allows secure access to patient medical records using QR codes. It provides both **public emergency access** for essential patient info and **private access** for doctors and administrators with full medical details.

---

## Features

- **Private Doctor/Admin Access**  
  - Full patient details (prescriptions, visits, contacts, insurance)  
  - Secure login with role-based access  

- **Public Emergency Access**  
  - Only essential patient information (blood group, allergies, emergency contacts)  
  - No login required  

- **QR Code Integration**  
  - Each patient has a unique QR code linking to their public page  
  - QR codes can be generated automatically from the database  

- **Secure Authentication**  
  - Users’ passwords are stored as bcrypt hashes  
  - Session management with Flask  

- **MongoDB Backend**  
  - Stores users, patients, prescriptions, and visits  

---

## Folder Structure

