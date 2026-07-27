"""
WorkoutExercise Schema

Responsible for:
1. Serializing WorkoutExercise objects.
2. Deserializing JSON requests.
3. Validating workout exercise data.
"""

from marshmallow import (
    Schema,
    fields,
    validate
)


class WorkoutExerciseSchema(Schema):

    id = fields.Integer(
        dump_only=True
    )

    workout_id = fields.Integer(
        required=True
    )

    exercise_id = fields.Integer(
        required=True
    )

    reps = fields.Integer(
        allow_none=True,
        validate=validate.Range(
            min=1,
            error="Reps must be greater than zero."
        )
    )

    sets = fields.Integer(
        allow_none=True,
        validate=validate.Range(
            min=1,
            error="Sets must be greater than zero."
        )
    )

    duration_seconds = fields.Integer(
        allow_none=True,
        validate=validate.Range(
            min=1,
            error="Duration must be greater than zero."
        )
    )


workout_exercise_schema = WorkoutExerciseSchema()

workout_exercises_schema = WorkoutExerciseSchema(
    many=True
)