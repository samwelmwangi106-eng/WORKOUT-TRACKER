# WORKOUT-TRACKER

A Flask REST API for tracking workouts and their associated exercises. The application allows users to create, update, retrieve, and delete workout sessions while maintaining relationships between workouts and exercises.

---

## Features

- Create workouts
- Retrieve all workouts
- Retrieve a single workout
- Update workout details
- Delete workouts
- Many-to-many relationship between workouts and exercises
- Data validation using Marshmallow
- SQLAlchemy ORM models
- Database migrations using Flask-Migrate
- SQLite database

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- SQLite

---

## Project Structure

```
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
│   │   └── workout.py
│   │
│   ├── schemas/
│   │   ├── workout_schema.py
│   │   ├── exercise_schema.py
│   │   └── workout_exercise_schema.py
│   │
│   └── instance/
│       └── app.db
│
├── requirements.txt
└── README.md
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

### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Database Setup

The SQLite database (`app.db`) is **not included** in this repository.

After cloning the project, create the database by running:

```bash
python -m flask --app server.app db upgrade
```

Populate the database with sample data:

```bash
python -m server.seed
```

---

## Running the Application

Start the Flask development server:

```bash
python -m server.app
```

The API will be available at:

```
http://127.0.0.1:5555
```

---

## API Endpoints

### Workouts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workouts` | Retrieve all workouts |
| GET | `/workouts/<id>` | Retrieve a single workout |
| POST | `/workouts` | Create a workout |
| PATCH | `/workouts/<id>` | Update a workout |
| DELETE | `/workouts/<id>` | Delete a workout |

---

## Example Request

### POST `/workouts`

```json
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

The API validates incoming data using Marshmallow and SQLAlchemy.

Examples include:

- Workout duration must be greater than 0.
- Exercise names must contain at least 3 characters.
- Required fields cannot be empty.
- Foreign key relationships are enforced by the database.

---

## Notes

- The SQLite database (`app.db`) is generated locally and is not tracked by Git.
- If you clone this repository, run the database migration before starting the server.
- Sample data can be added using the seed script.

---

## Author

**Samwel Macharia**