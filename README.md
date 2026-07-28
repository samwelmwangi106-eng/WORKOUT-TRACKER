# WORKOUT-TRACKER
 An API project that will be responsible for tracking workouts and their associated exercises.
# Workout Tracker API

A Flask REST API for tracking workouts and exercises. The application allows users to create, update, retrieve, and delete workout sessions while maintaining relationships between workouts and exercises.

---

## Features

- Create workouts
- View all workouts
- View a single workout
- Update workout details
- Delete workouts
- Many-to-many relationship between workouts and exercises
- Database migrations using Flask-Migrate
- Data validation using Marshmallow
- SQLAlchemy ORM models
- SQLite database

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite

---

## Project Structure

```
server/
│
├── app.py
├── extensions.py
├── models.py
├── seed.py
│
├── routes/
│   └── workout.py
│
├── schemas/
│   ├── workout_schema.py
│   ├── exercise_schema.py
│   └── workout_exercise_schema.py
│
└── instance/
    └── app.db
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd WORKOUT-TRACKER
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
source venv/Scripts/activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Initialize migrations

```bash
flask db init
```

Create a migration

```bash
flask db migrate -m "Initial migration"
```

Apply the migration

```bash
flask db upgrade
```

Seed the database

```bash
python3 server/seed.py
```

---

## Running the Application

Start the Flask server

```bash
python server/app.py
```

The API runs on

```
http://127.0.0.1:5555
```

---

## API Endpoints

### Workouts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /workouts | Retrieve all workouts |
| GET | /workouts/<id> | Retrieve a single workout |
| POST | /workouts | Create a workout |
| PATCH | /workouts/<id> | Update a workout |
| DELETE | /workouts/<id> | Delete a workout |

---

## Example Request

```json
POST /workouts

{
    "date": "2026-07-27",
    "duration_minutes": 60,
    "notes": "Leg day"
}
```

---

## Example Response

```json
{
    "id": 1,
    "date": "2026-07-27",
    "duration_minutes": 60,
    "notes": "Leg day"
}
```

---

## Data Validation

The application validates data using Marshmallow and SQLAlchemy.

Examples include:

- Workout duration must be greater than zero.
- Exercise names must contain at least three characters.
- Required fields cannot be empty.
- Foreign key relationships are enforced by the database.

---

## Author

Samwel Macharia