# Pharmacy Inventory API

## Description

A RESTful Pharmacy Inventory API built with FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication. The application allows users to register, authenticate, and securely manage pharmacy inventory through protected HTTP endpoints with full CRUD functionality, request validation, proper HTTP status codes, interactive API documentation, and automated integration testing.

---

## Features

- User registration
- Secure login with JWT authentication
- Password hashing with bcrypt
- Protected medicine endpoints
- View all medicines
- Search for a medicine by name (case-insensitive)
- Add new medicines
- Update medicine quantity
- Delete medicines
- Prevent duplicate NDC numbers
- Automatic request validation with Pydantic
- Response models for consistent API responses
- Proper HTTP status codes (201, 401, 404, 409, etc.)
- Interactive Swagger API documentation (`/docs`)
- Automated integration testing with pytest

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Psycopg
- Pydantic
- python-jose (JWT)
- Passlib (bcrypt)
- Uvicorn
- Pytest
- Git
- GitHub

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate a user and receive a JWT |
| GET | `/medicines` | Retrieve all medicines *(Requires authentication)* |
| GET | `/medicines/{name}` | Retrieve a medicine by name *(Requires authentication)* |
| POST | `/medicines` | Add a new medicine *(Requires authentication)* |
| PUT | `/medicines/{name}` | Update a medicine's quantity *(Requires authentication)* |
| DELETE | `/medicines/{name}` | Delete a medicine *(Requires authentication)* |

---

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

---

## Running Tests

Run the complete integration test suite with:

```bash
python -m pytest
```

The project includes **15 automated integration tests** covering:

- User registration
- User authentication
- Protected endpoints
- CRUD operations
- Duplicate validation
- Error handling

---

## Project Structure

```text
Pharmacy_inventory/
│
├── main.py              # FastAPI application and API endpoints
├── database.py          # SQLAlchemy database operations
├── models.py            # SQLAlchemy models
├── auth.py              # Password hashing and JWT authentication
├── test_api.py          # Pytest integration tests
├── requirements.txt
├── README.md
└── .gitignore
```

---

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
- [x] Implement JWT authentication and protected endpoints
- [x] Automated integration testing with pytest

### 🚧 Coming Next

- [ ] Environment variables (.env)
- [ ] Docker
- [ ] Cloud deployment