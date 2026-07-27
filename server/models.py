"""
models.py

This file contains:
1. The SQLAlchemy database object.
2. All database models (Workout, Exercise, WorkoutExercise).

For now, we only initialize SQLAlchemy.
We'll add the models in the next step.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Create a SQLAlchemy instance.
# It is initialized with the Flask app in app.py.
db = SQLAlchemy()

# Models will be added below.