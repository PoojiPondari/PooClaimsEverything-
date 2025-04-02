PooClaimsEverything! – Insurance Cost Predictor
PooClaimsEverything! is an intelligent web application built with Flask that leverages machine learning to predict insurance costs based on personal health factors. The app is designed to help users get accurate cost predictions with a focus on privacy and security.

Key Features:
AI-powered Predictions: Instant insurance cost predictions using machine learning.

Personal Dashboard: View your prediction history and track changes over time.

Real-Time BMI Calculation: Automatically calculates and validates BMI for users.

Secure Authentication: Protects your data with secure login and encrypted storage.

Mobile & Desktop Friendly: Fully responsive, ensuring ease of use across devices.

Login History Tracking: Monitors and stores login attempts for better security.

Quick Start:
Clone the Repository
Clone the project using Git and navigate to the project directory.

Set Up Virtual Environment
Create and activate a virtual environment:

bash
Copy
python -m venv venv  
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install Dependencies
Install the required libraries with:

bash
Copy
pip install -r requirements.txt
Run the Application
Start the app by running:

bash
Copy
python run.py
Access the App
Open a web browser and go to http://localhost:5000 to use the app.

User Input Parameters:
Age: Between 1 to 70 years

BMI: Minimum 20

Children: 0 to 5

Smoker: Yes / No

Region: Northeast, Northwest, Southeast, Southwest

Security Features:
Password Encryption: Ensures user credentials are securely stored.

CSRF Protection: Prevents cross-site request forgery attacks.

Session Management: Uses Flask-Login for handling user sessions.

Login History Monitoring: Tracks login times, IP addresses, and user agent details.

Technology Stack:
Backend: Flask, Flask-Login, SQLAlchemy

Machine Learning: scikit-learn

Frontend: Bootstrap for responsive design

Database: SQLite (or any relational DB)

Form Validation: WTForms for secure form handling

Database Schema:
User Model: Stores username, email, password, and claims data.

Claims Model: Tracks user-related claims information, including age, BMI, smoker status, and predicted charges.

Login History Model: Captures the timestamp, IP address, and status of login attempts.

Future Enhancements:
Additional Prediction Factors: Introduce more variables to improve predictions.

API Integration: Expose prediction functionality via API endpoints.

Data Visualization: Visualize predictions and user data trends.

Social Authentication: Allow users to log in via Google or GitHub.

Export Data: Enable users to export their prediction history.

Admin Dashboard: Develop an admin panel for managing users and monitoring activity.
