"""
extensions.py

This file creates shared Flask extensions.

Responsibilities:
1. SQLAlchemy database
2. Flask-Migrate
3. Marshmallow
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


# Database object
db = SQLAlchemy()

# Migration object
migrate = Migrate()

# Marshmallow object
ma = Marshmallow()