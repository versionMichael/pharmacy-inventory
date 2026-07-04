# Pharmacy Inventory API

## Description

A RESTful Pharmacy Inventory API built with FastAPI and SQLite. The application allows users to manage pharmacy inventory through HTTP endpoints with full CRUD functionality, request validation, proper HTTP status codes, and interactive API documentation.

## Features

- View all medicines
- Search for a medicine by name
- Add new medicines
- Update medicine quantity
- Delete medicines
- Prevent duplicate NDC numbers
- Automatic request validation with Pydantic
- Proper HTTP status codes (201, 404, 409, etc.)
- Interactive Swagger documentation (`/docs`)

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- Git
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/medicines` | Get all medicines |
| GET | `/medicines/{name}` | Search for a medicine |
| POST | `/medicines` | Add a medicine |
| PUT | `/medicines/{name}` | Update medicine quantity |
| DELETE | `/medicines/{name}` | Remove a medicine |

## How to Run

1. Clone the repository.
2. Install dependencies:

```bash
pip install fastapi uvicorn
```

3. Start the API:

```bash
python -m uvicorn main:app --reload
```

4. Open your browser and navigate to:

```
http://127.0.0.1:8000/docs
```

## Roadmap Progress

### ✅ Completed

- [x] Replace text file storage with SQLite
- [x] Convert command-line application to a FastAPI REST API
- [x] Implement CRUD API endpoints
- [x] Add request validation with Pydantic
- [x] Add proper HTTP status codes
- [x] Add response models

### 🚧 In Progress

- [ ] Migrate from SQLite to PostgreSQL
- [ ] Replace raw SQL with SQLAlchemy
- [ ] Add JWT authentication
- [ ] Dockerize the application
- [ ] Deploy to the cloud
- [ ] Add automated tests