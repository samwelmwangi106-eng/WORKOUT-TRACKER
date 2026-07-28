"""
models.py

Contains:
1. Workout model
2. Exercise model
3. WorkoutExercise join model
4. Relationships
5. Constraints
6. Model validations
"""

from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

from extensions import db




# Workout Model


class Workout(db.Model):
    """
    Represents a workout session.

    Examples:
    - Push Day
    - Leg Day
    - Full Body
    """

    __tablename__ = "workouts"


    __table_args__ = (
        CheckConstraint(
            "duration_minutes > 0",
            name="check_duration_positive"
        ),
    )


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    date = db.Column(
        db.Date,
        nullable=False
    )


    duration_minutes = db.Column(
        db.Integer,
        nullable=False
    )


    notes = db.Column(
        db.Text
    )


    # One workout has many WorkoutExercise records
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )


    # Many-to-many relationship with Exercise
    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercises",
        viewonly=True
    )



    # Validation
    @validates("duration_minutes")
    def validate_duration(self, key, value):

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



    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )


    category = db.Column(
        db.String(50),
        nullable=False
    )


    equipment_needed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )



    # One exercise has many WorkoutExercise records
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )


    # Many-to-many relationship with Workout
    workouts = db.relationship(
        "Workout",
        secondary="workout_exercises",
        viewonly=True
    )



    # Validation
    @validates("name")
    def validate_name(self, key, value):

        value = value.strip()


        if not value:
            raise ValueError(
                "Exercise name cannot be empty."
            )


        if len(value) < 3:
            raise ValueError(
                "Exercise name must be at least 3 characters."
            )


        return value.title()





# WorkoutExercise Join Model


class WorkoutExercise(db.Model):
    """
    Join table between Workout and Exercise.

    Stores workout-specific information:
    - sets
    - reps
    - duration
    """

    __tablename__ = "workout_exercises"



    id = db.Column(
        db.Integer,
        primary_key=True
    )



    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )



    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )



    reps = db.Column(
        db.Integer
    )


    sets = db.Column(
        db.Integer
    )


    duration_seconds = db.Column(
        db.Integer
    )



    # Relationship back to Workout
    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )


    # Relationship back to Exercise
    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )



    # Validation
    @validates(
        "reps",
        "sets",
        "duration_seconds"
    )
    def validate_positive_values(self, key, value):

        if value is not None and value <= 0:
            raise ValueError(
                f"{key} must be greater than zero."
            )

        return value