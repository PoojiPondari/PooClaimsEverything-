from app import create_app, db
from app.models import User, ClaimsData  # Import the models

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # This will create all tables based on the models
        db.drop_all()  # Drop all existing tables
        db.create_all()  # Create new tables with updated schema
    app.run(debug=True) 