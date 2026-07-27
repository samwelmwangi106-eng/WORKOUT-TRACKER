from flask import Blueprint, request, jsonify

from models import Workout
from datetime import datetime
from extensions import db


# Create Blueprint
# Groups all workout-related routes

workout_bp = Blueprint(
    "workout",
    __name__
)



# ==========================================
# GET ALL WORKOUTS
# METHOD: GET
# URL: /workouts
# ==========================================

@workout_bp.route("/workouts", methods=["GET"])
def get_workouts():

    workouts = Workout.query.all()


    return jsonify(
        [
            {
                "id": workout.id,
                "date": workout.date,
                "duration_minutes": workout.duration_minutes,
                "notes": workout.notes
            }

            for workout in workouts
        ]
    )




# ==========================================
# GET ONE WORKOUT
# METHOD: GET
# URL: /workouts/<id>
# ==========================================

@workout_bp.route("/workouts/<int:id>", methods=["GET"])
def get_one_workout(id):

    workout = Workout.query.get(id)


    if not workout:

        return {
            "error": "Workout not found"
        }, 404



    return {

        "id": workout.id,
        "date": workout.date,
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes

    }




# ==========================================
# CREATE WORKOUT
# METHOD: POST
# URL: /workouts
# ==========================================

@workout_bp.route("/workouts", methods=["POST"])
def create_workout():

    data = request.get_json()


    workout = Workout(

        date=data["date"],

        duration_minutes=data["duration_minutes"],

        notes=data.get("notes")

    )


    db.session.add(workout)

    db.session.commit()



    return {

        "message": "Workout created",

        "id": workout.id

    }, 201




# ==========================================
# UPDATE WORKOUT
# METHOD: PATCH
# URL: /workouts/<id>
# ==========================================

@workout_bp.route("/workouts/<int:id>", methods=["PATCH"])
def update_workout(id):

    workout = Workout.query.get(id)


    if not workout:

        return {
            "error": "Workout not found"
        }, 404



    data = request.get_json()



    if "date" in data:
        workout.date = data["date"]


    if "duration_minutes" in data:
        workout.duration_minutes = data["duration_minutes"]


    if "notes" in data:
        workout.notes = data["notes"]



    db.session.commit()



    return {

        "message": "Workout updated"

    }




# ==========================================
# DELETE WORKOUT
# METHOD: DELETE
# URL: /workouts/<id>
# ==========================================

@workout_bp.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):

    workout = Workout.query.get(id)


    if not workout:

        return {
            "error": "Workout not found"
        },404



    db.session.delete(workout)

    db.session.commit()



    return {

        "message": "Workout deleted"

    }