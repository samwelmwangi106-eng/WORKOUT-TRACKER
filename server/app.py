"""
app.py

This is the application's entry point.

Responsibilities:
1. Create the Flask application.
2. Configure the SQLite database.
3. Initialize SQLAlchemy.
4. Enable Flask-Migrate.
5. Register routes (later).
"""

from flask import Flask
from flask_migrate import Migrate

from models import db

# Create the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# Disable modification tracking to improve performance
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect SQLAlchemy to the Flask app
db.init_app(app)

# Enable database migrations
migrate = Migrate(app, db)


@app.route("/")
def home():
    """
    Test route to confirm the API is running.
    """
    return {
        "message": "Workout Tracker API is running!"
    }


if __name__ == "__main__":
    app.run(port=5555, debug=True)