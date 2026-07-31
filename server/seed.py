"""
seed.py

Run this once to create the database and populate it with sample data.

    python3 server/seed.py

Safe to re-run:
The database is checked first. If data already exists,
the seed operation is skipped to avoid duplicates.
"""

from datetime import date

from server.app import app, db
from server.models import Workout, Exercise, WorkoutExercise



def seed():
    with app.app_context():

     
        # 1. Create all database tables
       
        # If the tables already exist, nothing happens.
        db.create_all()

       
        # 2. Prevent duplicate seed data
       
        if Workout.query.first():
            print("Database already contains data. Skipping seed.")
            return

        
        # 3. Create workouts
       
        upper_body = Workout(
            date=date(2026, 7, 28),
            duration_minutes=60,
            notes="Upper body strength workout"
        )

        leg_day = Workout(
            date=date(2026, 7, 29),
            duration_minutes=45,
            notes="Lower body workout"
        )

       
        # 4. Create exercises
       
        push_up = Exercise(
            name="Push Up",
            category="Chest",
            equipment_needed=False
        )

        squat = Exercise(
            name="Squat",
            category="Legs",
            equipment_needed=False
        )

        plank = Exercise(
            name="Plank",
            category="Core",
            equipment_needed=False
        )

        # Save workouts and exercises first
        db.session.add_all([
            upper_body,
            leg_day,
            push_up,
            squat,
            plank
        ])

        # Commit so they receive database IDs
        db.session.commit()

        
        # 5. Link exercises to workouts
        
        workout_exercises = [

            WorkoutExercise(
                workout_id=upper_body.id,
                exercise_id=push_up.id,
                sets=3,
                reps=15
            ),

            WorkoutExercise(
                workout_id=upper_body.id,
                exercise_id=squat.id,
                sets=4,
                reps=12
            ),

            WorkoutExercise(
                workout_id=leg_day.id,
                exercise_id=plank.id,
                duration_seconds=60
            )
        ]

        db.session.add_all(workout_exercises)
        db.session.commit()

        print("Database seeded successfully!")
        print("Created:")
        print("- 2 Workouts")
        print("- 3 Exercises")
        print("- 3 WorkoutExercise records")


if __name__ == "__main__":
    seed()