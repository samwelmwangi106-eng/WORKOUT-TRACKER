#  Workout Tracker API

A RESTful API built with **Flask**, **SQLAlchemy**, and **Marshmallow** for managing workout sessions and exercises.

The application allows users to create workouts, manage reusable exercises, and associate exercises with workouts through a many-to-many relationship.

---

## Features

-  Full CRUD operations for Workouts
-  Full CRUD operations for Exercises
-  Full CRUD operations for WorkoutExercise records
-  Many-to-many relationship between Workouts and Exercises
-  SQLAlchemy ORM models
-  Marshmallow serialization & deserialization
-  Schema validations
-  Model validations
-  Database constraints
-  Flask-Migrate database migrations
-  Seed script with sample data

---

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- SQLite

---

## Project Structure

```text
WORKOUT-TRACKER/
│
├── migrations/
│
├── server/
│   ├── app.py
│   ├── extensions.py
│   ├── models.py
│   ├── seed.py
│   │
│   ├── routes/
│   │   ├── workout.py
│   │   ├── excercise.py
│   │   └── workout_exercise.py
│   │
│   ├── schemas/
│   │   ├── workout_schema.py
│   │   ├── excercise_schema.py
│   │   └── workout_exercise_schema.py
│   │
│   └── instance/
│       └── app.db
│
├── migrations/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd WORKOUT-TRACKER
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Git Bash

```bash
source venv/Scripts/activate
```

### Windows CMD

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Run the database migrations

```bash
python -m flask --app server.app db upgrade
```

Populate the database with sample data

```bash
python -m server.seed
```

---

# Running the Application

Start the development server

```bash
python -m server.app
```

The API will be available at

```
http://127.0.0.1:5555
```

---

# API Endpoints

## Workout Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/workouts` | Get all workouts |
| GET | `/workouts/<id>` | Get one workout |
| POST | `/workouts` | Create workout |
| PATCH | `/workouts/<id>` | Update workout |
| DELETE | `/workouts/<id>` | Delete workout |

---

## Exercise Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/exercises` | Get all exercises |
| GET | `/exercises/<id>` | Get one exercise |
| POST | `/exercises` | Create exercise |
| PATCH | `/exercises/<id>` | Update exercise |
| DELETE | `/exercises/<id>` | Delete exercise |

---

## WorkoutExercise Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/workout-exercises` | Get all workout exercises |
| GET | `/workout-exercises/<id>` | Get one workout exercise |
| POST | `/workout-exercises` | Create workout exercise |
| PATCH | `/workout-exercises/<id>` | Update workout exercise |
| DELETE | `/workout-exercises/<id>` | Delete workout exercise |

---

# Example Request

### POST `/workouts`

```json
{
  "date": "2026-07-27",
  "duration_minutes": 60,
  "notes": "Leg Day"
}
```

---

# Example Response

```json
{
  "id": 1,
  "date": "2026-07-27",
  "duration_minutes": 60,
  "notes": "Leg Day"
}
```

---

# Validations

### Schema Validations

- Workout duration must be greater than 0.
- Exercise name must contain at least 3 characters.
- Exercise category cannot be empty.
- Sets, reps and duration must be greater than 0.

### Model Validations

- Workout duration cannot be zero or negative.
- Exercise names are trimmed and formatted.
- Positive values are enforced for reps, sets and duration.

### Database Constraints

- Workout duration must be positive.
- Exercise names are unique.
- Foreign key constraints maintain relationships.

---

# Seed Data

Run

```bash
python -m server.seed
```

The script creates

- 2 Workouts
- 3 Exercises
- 3 WorkoutExercise records

The seed file is safe to run multiple times and avoids inserting duplicate data.

---

# Author

**Samwel Macharia**

---

