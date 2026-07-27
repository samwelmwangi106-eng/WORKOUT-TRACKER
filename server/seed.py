#!/usr/bin/env python3

"""
seed.py

This file will populate the database with sample data.
"""

from app import app

with app.app_context():
    print("Ready to seed the database.")