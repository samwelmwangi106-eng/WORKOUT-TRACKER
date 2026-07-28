"""
workout_schema.py

Contains the schema used to:

1. Serialize Workout objects into JSON.
2. Deserialize JSON into Workout objects.
3. Validate incoming API data.
"""

from marshmallow import fields, validate
from flask_marshmallow import SQLAlchemyAutoSchema

from models import Workout
from extensions import db


class WorkoutSchema(SQLAlchemyAutoSchema):
    """
    Schema for the Workout model.
    """

    class Meta:
        model = Workout
        load_instance = True
        sqla_session = db.session


   
    # Fields
    

    id = fields.Integer(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Integer(
        required=True,
        validate=validate.Range(
            min=1,
            error="Workout must be at least 1 minute."
        )
    )

    notes = fields.String(
        allow_none=True
    )