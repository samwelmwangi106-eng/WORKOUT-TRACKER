from flask import Blueprint, request
from marshmallow import ValidationError

from server.extensions import db
from server.models import WorkoutExercise
from server.schemas.workout_exercise_schema import (
    workout_exercise_schema,
    workout_exercises_schema
)

workout_exercise_bp = Blueprint(
    "workout_exercise",
    __name__
)



# GET ALL WORKOUT EXERCISES


@workout_exercise_bp.route("/workout-exercises", methods=["GET"])
def get_workout_exercises():

    workout_exercises = WorkoutExercise.query.all()

    return workout_exercises_schema.dump(workout_exercises), 200



# GET ONE WORKOUT EXERCISE


@workout_exercise_bp.route("/workout-exercises/<int:id>", methods=["GET"])
def get_one_workout_exercise(id):

    workout_exercise = WorkoutExercise.query.get(id)

    if not workout_exercise:
        return {"error": "Workout exercise not found"}, 404

    return workout_exercise_schema.dump(workout_exercise), 200



# CREATE WORKOUT EXERCISE


@workout_exercise_bp.route("/workout-exercises", methods=["POST"])
def create_workout_exercise():

    try:
        data = workout_exercise_schema.load(request.get_json())

    except ValidationError as err:
        return err.messages, 400

    workout_exercise = WorkoutExercise(**data)

    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise_schema.dump(workout_exercise), 201



# UPDATE WORKOUT EXERCISE


@workout_exercise_bp.route("/workout-exercises/<int:id>", methods=["PATCH"])
def update_workout_exercise(id):

    workout_exercise = WorkoutExercise.query.get(id)

    if not workout_exercise:
        return {"error": "Workout exercise not found"}, 404

    try:
        data = workout_exercise_schema.load(
            request.get_json(),
            partial=True
        )

    except ValidationError as err:
        return err.messages, 400

    for key, value in data.items():
        setattr(workout_exercise, key, value)

    db.session.commit()

    return workout_exercise_schema.dump(workout_exercise), 200



# DELETE WORKOUT EXERCISE


@workout_exercise_bp.route("/workout-exercises/<int:id>", methods=["DELETE"])
def delete_workout_exercise(id):

    workout_exercise = WorkoutExercise.query.get(id)

    if not workout_exercise:
        return {"error": "Workout exercise not found"}, 404

    db.session.delete(workout_exercise)
    db.session.commit()

    return {"message": "Workout exercise deleted"}, 200