"""
models.py

This file contains:

1. The SQLAlchemy database instance.
2. Workout model.
3. Exercise model.
4. WorkoutExercise model.
5. Relationships between the models.
6. Table constraints.
7. Model validations.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

# Create the SQLAlchemy database object.
# It will be initialized inside app.py.
db = SQLAlchemy()



# Workout Model

class Workout(db.Model):
    """
    Represents a workout session.
    Example:
        - Push Day
        - Leg Day
        - Full Body
    """

    __tablename__ = "workouts"

    # Table constraint:
    # Every workout must have a duration greater than zero.
    __table_args__ = (
        CheckConstraint(
            "duration_minutes > 0",
            name="check_duration_positive"
        ),
    )

    
    id = db.Column(db.Integer, primary_key=True)

   
    date = db.Column(db.Date, nullable=False)

    
    duration_minutes = db.Column(
        db.Integer,
        nullable=False
    )

    # Optional notes
    notes = db.Column(db.Text)

    
    # Relationships
    

    # One Workout has many WorkoutExercise records.
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    # A Workout has many Exercises through WorkoutExercise.
    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercises",
        viewonly=True
    )

    # Model Validation
    
    @validates("duration_minutes")
    def validate_duration(self, key, value):
        """
        Ensure workout duration is greater than zero.
        """
        if value <= 0:
            raise ValueError(
                "Workout duration must be greater than 0 minutes."
            )

        return value


# Exercise Model
class Exercise(db.Model):
    """
    Represents a reusable exercise.

    Examples:
        - Push-up
        - Squat
        - Deadlift
    """

    __tablename__ = "exercises"

   
    id = db.Column(db.Integer, primary_key=True)

   
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    
    category = db.Column(
        db.String(50),
        nullable=False
    )

    # Whether equipment is required
    equipment_needed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    # Relationships
    

    # One Exercise has many WorkoutExercise records.
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    # An Exercise belongs to many Workouts.
    workouts = db.relationship(
        "Workout",
        secondary="workout_exercises",
        viewonly=True
    )

   
    # Model Validation
    
    @validates("name")
    def validate_name(self, key, value):
        """
        Ensure the exercise name is valid.
        """
        if not value.strip():
            raise ValueError(
                "Exercise name cannot be empty."
            )

        if len(value.strip()) < 3:
            raise ValueError(
                "Exercise name must be at least 3 characters long."
            )

        return value.title()



# WorkoutExercise Model (Join Table)

class WorkoutExercise(db.Model):
    """
    Join table connecting Workouts and Exercises.

    Stores workout-specific information such as:
        - reps
        - sets
        - duration_seconds
    """

    __tablename__ = "workout_exercises"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Foreign Key → Workout table
    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    # Foreign Key → Exercise table
    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    # Workout details
    reps = db.Column(db.Integer)

    sets = db.Column(db.Integer)

    duration_seconds = db.Column(db.Integer)

    
    # Relationships
   

    # Each WorkoutExercise belongs to one Workout.
    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    # Each WorkoutExercise belongs to one Exercise.
    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )