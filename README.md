🧠 PooClaimsEverything! – Smarter Insurance Cost Predictions
PooClaimsEverything is a simple and secure web app built with Flask that helps users predict their insurance costs based on personal health data. It uses machine learning to give fast, accurate estimates—no spreadsheets, no guessing!

🔍 What Can It Do?
Predicts insurance costs instantly using AI

Provides a personal dashboard with history

Calculates your BMI in real-time

Tracks login history and secures your data

Works smoothly on mobile and desktop

🚀 How to Get Started
Clone the repo
git clone https://github.com/yourusername/insurance-claim-predictor.git

Create a virtual environment
python -m venv venv
Activate it: venv\Scripts\activate (Windows)

Install dependencies
pip install -r requirements.txt

Start the app

bash
Copy
python setup_images.py  # (optional for setting up images)
python run.py
Visit in browser
Open http://localhost:5000

🧾 User Inputs
Age: 1 to 70

BMI: Must be at least 20

Children: 0 to 5

Smoker: Yes / No

Region: NE, NW, SE, SW

🛡️ Built-in Security
Encrypted passwords

CSRF protection via Flask-WTF

Session management with Flask-Login

Login tracking (time, IP, status)

🧱 Tech Stack
Flask + Flask-Login + SQLAlchemy

ML with scikit-learn

Bootstrap + Toastify for UI

WTForms for validation

SQLite or other SQL database

🗃️ Database Overview
User: username, email, password, claims
Claims: age, BMI, smoker, region, predicted charges
Login Logs: time, IP, user agent, success

💡 Cool Features
Age and BMI-based risk insights

Smoker impact factored in predictions

Clean, responsive UI

Prediction logging for learning and analysis

📌 Future Plans
Add charts and graphs

REST API support

Social login (Google, GitHub)

Export claim reports

Admin dashboard

🧩 Project Layout
arduino
Copy
app/
│── static/images/
│── templates/
│   ├── login.html, dashboard.html, predict.html, etc.
│── __init__.py
│── routes.py
│── models.py
│── forms.py
│── ml_model.py
├── run.py
├── requirements.txt
├── setup_images.py

MIT License.
