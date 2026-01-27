# FastAPI Clean Architecture Project

This is a FastAPI project implementing Clean Architecture principles with CRUD operations for products.

## Architecture

The project follows a layered architecture:

- **Domain Layer** (`src/domain`): Contains logic-free business entities and repository interfaces.
- **Application Layer** (`src/application`): Contains use cases that orchestrate business logic.
- **Infrastructure Layer** (`src/infrastructure`): Contains frameworks, drivers, and tools (Database, etc.).
- **Presentation Layer** (`src/presentation`): Contains the API implementation (routes, schemas).

## Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Modify `.env` if you want to use a different database (defaults to SQLite).

## Running the Application

To run the application with hot-reload enabled (for development):

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`.

## API Documentation

Interactive API documentation is available at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

- **GET /api/v1/products**: List all products
- **POST /api/v1/products**: Create a new product
- **GET /api/v1/products/{id}**: Get a product by ID
- **PUT /api/v1/products/{id}**: Update a product
- **DELETE /api/v1/products/{id}**: Delete a product
