"""
app.py

Application entry point.

Responsibilities:
1. Create Flask application.
2. Configure database.
3. Initialize extensions.
4. Register routes.
"""
import os
instance_path = os.path.join(os.path.dirname(__file__), "instance")

os.makedirs(instance_path, exist_ok=True)
from flask import Flask

from server.extensions import db, migrate, ma


# Create Flask application

app = Flask(__name__)



# Database configuration

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, "instance", "app.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# Initialize extensions

db.init_app(app)

migrate.init_app(app, db)
ma.init_app(app)
with app.app_context():
    print("Instance path:", app.instance_path)
    print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])
    print("Engine URL:", db.engine.url)



# # Import models after db initialization

from server.models import Workout, Exercise, WorkoutExercise



# Import routes

from server.routes.workout import workout_bp



# Register routes

app.register_blueprint(workout_bp)




# Test route

@app.route("/")
def home():

    return {
        "message": "Workout Tracker API is running!"
    }




if __name__ == "__main__":

    app.run(
        port=5555,
        debug=True
    )