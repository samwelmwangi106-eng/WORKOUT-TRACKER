"""
app.py

Application entry point.

Responsibilities:
1. Create Flask application.
2. Configure database.
3. Initialize extensions.
4. Register routes.
"""

from flask import Flask

from extensions import db, migrate



# Create Flask application

app = Flask(__name__)



# Database configuration

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# Initialize extensions

db.init_app(app)

migrate.init_app(app, db)



# # Import models after db initialization

# from models import Workout, Exercise, WorkoutExercise



# Import routes

from routes.workout import workout_bp



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