"""
Exercise Schema

Responsible for:
1. Serializing Exercise objects.
2. Deserializing JSON requests.
3. Validating incoming exercise data.
"""

from marshmallow import (
    Schema,
    fields,
    validate,
    validates,
    ValidationError
)


class ExerciseSchema(Schema):

    id = fields.Integer(
        dump_only=True
    )

    name = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=100
        )
    )

    category = fields.String(
        required=True
    )

    equipment_needed = fields.Boolean(
        required=True
    )

    @validates("category")
    def validate_category(self, value):

        if not value.strip():

            raise ValidationError(
                "Category cannot be empty."
            )


exercise_schema = ExerciseSchema()

exercises_schema = ExerciseSchema(many=True)