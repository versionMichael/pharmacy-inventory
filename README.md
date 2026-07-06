# Pharmacy Inventory API

## Description

A RESTful Pharmacy Inventory API built with FastAPI, PostgreSQL, and SQLAlchemy. The application allows users to manage pharmacy inventory through HTTP endpoints with full CRUD functionality, request validation, proper HTTP status codes, and interactive API documentation.

## Features

- View all medicines
- Search for a medicine by name (case-insensitive)
- Add new medicines
- Update medicine quantity
- Delete medicines
- Prevent duplicate NDC numbers
- Automatic request validation with Pydantic
- Response models for consistent API responses
- Proper HTTP status codes (201, 404, 409, etc.)
- Interactive Swagger API documentation (`/docs`)

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Psycopg
- Pydantic
- Uvicorn
- Git
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/medicines` | Retrieve all medicines |
| GET | `/medicines/{name}` | Retrieve a medicine by name |
| POST | `/medicines` | Add a new medicine |
| PUT | `/medicines/{name}` | Update a medicine's quantity |
| DELETE | `/medicines/{name}` | Delete a medicine |

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Pharmacy_inventory
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a PostgreSQL database named:

```
pharmacy_inventory
```

4. Update the database connection settings in `database.py`:

```python
DATABASE_URL = "postgresql+psycopg://YOUR_USERNAME:YOUR_PASSWORD@localhost/pharmacy_inventory"
```

5. Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

6. Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

## Project Structure

```text
Pharmacy_inventory/
│
├── main.py              # FastAPI application and API endpoints
├── database.py          # SQLAlchemy database operations
├── models.py            # SQLAlchemy models
├── requirements.txt
├── README.md
└── .gitignore
```

## Roadmap Progress

### ✅ Completed

- [x] Build command-line pharmacy inventory application
- [x] Replace text file storage with SQLite
- [x] Convert application to a FastAPI REST API
- [x] Implement CRUD API endpoints
- [x] Add request validation with Pydantic
- [x] Add response models
- [x] Return proper HTTP status codes
- [x] Migrate from SQLite to PostgreSQL
- [x] Refactor raw SQL to SQLAlchemy ORM
- [x] Implement case-insensitive medicine searches

### 🚧 Coming Next

- [ ] JWT Authentication
- [ ] Docker
- [ ] Cloud Deployment
- [ ] Automated Testing