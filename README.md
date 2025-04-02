PooClaimsEverything! – Insurance Cost Predictor

PooClaimsEverything is a Flask web app that predicts insurance costs based on personal health data. It uses machine learning to provide quick, accurate estimates.

Key Features:
Predicts insurance costs using AI

Provides a personal dashboard with prediction history

Calculates BMI in real-time

Secure user login and data protection

Works on both mobile and desktop

How to Get Started:
Clone the repository.

Set up a virtual environment and activate it.

Install the required dependencies with pip install -r requirements.txt.

Start the application with python run.py.

Open your browser and go to http://localhost:5000 to access the app.

User Inputs:
Age: 1 to 70 years

BMI: Minimum 20

Children: 0 to 5

Smoker: Yes / No

Region: Northeast, Northwest, Southeast, Southwest

Security Features:
Passwords are encrypted

CSRF protection

Login tracking (including time, IP, and status)

Tech Stack:
Flask with Flask-Login and SQLAlchemy

Machine Learning using scikit-learn

Bootstrap for UI

WTForms for form validation

SQLite or other SQL database

Database Structure:
User: username, email, password, claims

Claims: age, BMI, children, smoker, region, predicted charges

Login Logs: time, IP, user agent, status

Future Features:
Add more prediction factors

Implement API endpoints

Add data visualization

Enable social login options

Export functionality

Admin dashboard

