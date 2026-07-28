"""
Workout Routes

Contains CRUD endpoints for Workout.
"""

from flask import Blueprint, request

from marshmallow import ValidationError

from models import Workout
from extensions import db

from schemas.workout_schema import (
    workout_schema,
    workouts_schema
)



# Blueprint


workout_bp = Blueprint(
    "workout",
    __name__
)



# GET ALL WORKOUTS
# METHOD: GET
# URL: /workouts


@workout_bp.route("/workouts", methods=["GET"])
def get_workouts():

    workouts = Workout.query.all()

    return workouts_schema.dump(workouts), 200



# GET ONE WORKOUT
# METHOD: GET
# URL: /workouts/<id>


@workout_bp.route("/workouts/<int:id>", methods=["GET"])
def get_one_workout(id):

    workout = Workout.query.get(id)

    if workout is None:
        return {
            "error": "Workout not found"
        }, 404

    return workout_schema.dump(workout), 200



# CREATE WORKOUT
# METHOD: POST
# URL: /workouts


@workout_bp.route("/workouts", methods=["POST"])
def create_workout():

    try:
        data = workout_schema.load(
            request.get_json()
        )

    except ValidationError as err:
        return {
            "errors": err.messages
        }, 400

    workout = Workout(**data)

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201



# UPDATE WORKOUT
# METHOD: PATCH
# URL: /workouts/<id>


@workout_bp.route("/workouts/<int:id>", methods=["PATCH"])
def update_workout(id):

    workout = Workout.query.get(id)

    if workout is None:
        return {
            "error": "Workout not found"
        }, 404

    try:
        data = workout_schema.load(
            request.get_json(),
            partial=True
        )

    except ValidationError as err:
        return {
            "errors": err.messages
        }, 400

    for key, value in data.items():
        setattr(workout, key, value)

    db.session.commit()

    return workout_schema.dump(workout), 200



# DELETE WORKOUT
# METHOD: DELETE
# URL: /workouts/<id>


@workout_bp.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):

    workout = Workout.query.get(id)

    if workout is None:
        return {
            "error": "Workout not found"
        }, 404

    db.session.delete(workout)
    db.session.commit()

    return {
        "message": "Workout deleted successfully"
    }, 200