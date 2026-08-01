from flask import Blueprint, request
from marshmallow import ValidationError

from server.extensions import db
from server.models import Exercise
from server.schemas.excercise_schema import (
    exercise_schema,
    exercises_schema
)

exercise_bp = Blueprint(
    "exercise",
    __name__
)



# GET ALL EXERCISES


@exercise_bp.route("/exercises", methods=["GET"])
def get_exercises():

    exercises = Exercise.query.all()

    return exercises_schema.dump(exercises), 200



# GET ONE EXERCISE


@exercise_bp.route("/exercises/<int:id>", methods=["GET"])
def get_one_exercise(id):

    exercise = Exercise.query.get(id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    return exercise_schema.dump(exercise), 200



# CREATE EXERCISE


@exercise_bp.route("/exercises", methods=["POST"])
def create_exercise():

    try:
        data = exercise_schema.load(request.get_json())

    except ValidationError as err:
        return err.messages, 400

    exercise = Exercise(**data)

    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.dump(exercise), 201



# UPDATE EXERCISE


@exercise_bp.route("/exercises/<int:id>", methods=["PATCH"])
def update_exercise(id):

    exercise = Exercise.query.get(id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    try:
        data = exercise_schema.load(
            request.get_json(),
            partial=True
        )

    except ValidationError as err:
        return err.messages, 400

    for key, value in data.items():
        setattr(exercise, key, value)

    db.session.commit()

    return exercise_schema.dump(exercise), 200



# DELETE EXERCISE


@exercise_bp.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):

    exercise = Exercise.query.get(id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    db.session.delete(exercise)
    db.session.commit()

    return {"message": "Exercise deleted"}, 200