# Async Article Microservice (OAuth2)

## Overview

The Async Article Microservice is a RESTful API built using FastAPI, designed for handling CRUD operations on Articles. It leverages asynchronous capabilities using SQLAlchemy and PostgreSQL for better performance and scalability.

## Features

- Create, read, update, and delete Articles.
- Fully asynchronous operations.
- JWT authentication to secure endpoints.
- Integration with an Authentication Service for user authentication and authorization.
- Alembic for database migrations

## Technologies Used

- **FastAPI**: Web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: Relational database management system.
- **asyncpg**: Asyncio PostgreSQL driver for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **JWT**: JSON Web Tokens for authentication.

## Requirements

- Python 3.8+
- PostgreSQL
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/your-repo/fastapi-async-sqlalchemy-postgresql.git
cd fastapi-async-sqlalchemy-postgresql
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```
DATABASE_URL=postgresql+asyncpg://username:password@localhost/dbname
SECRET_KEY=your_secret_key
```

Replace `username`, `password`, `localhost`, and `dbname` with your PostgreSQL credentials and database name.

### 5. Database Setup

Ensure your PostgreSQL server is running and create the necessary database.

Run Database Migrations

```sh
alembic upgrade head
```
Now you have a database with all the migrations applied.

### 6. Run the Application

Start the FastAPI application using Uvicorn:

```sh
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Authentication Endpoints

These endpoints are provided by the Authentication Service:

- **POST /auth/login**: User login to get JWT token.
- **POST /auth/register**: User registration.

### Post Endpoints

All Article endpoints are secured and require a valid JWT token in the `Authorization` header.

- **GET /api/articles/**: Get a list of all articles.
- **GET /api/articles/{article_id}**: Get a specific article by ID.
- **POST /api/articles/**: Create a new article.
- **PUT /api/articles/{article_id}**: Update a specific article by ID.
- **DELETE /api/articles/{article_id}**: Delete a specific article by ID.

### Example cURL Requests

#### Create a Article

```sh
curl -X POST "http://127.0.0.1:8000/api/articles/" -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{
  "title": "My First Post",
  "content": "Content of my first article"
}'
```

#### Get All Articles

```sh
curl -X GET "http://127.0.0.1:8000/api/articles/" -H "Authorization: Bearer <your_jwt_token>"
```

#### Get a Article by ID

```sh
curl -X GET "http://127.0.0.1:8000/api/articles/1" -H "Authorization: Bearer <your_jwt_token>"
```

#### Update a Article

```sh
curl -X PUT "http://127.0.0.1:8000/api/articles/1" -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{
  "title": "Updated Title",
  "content": "Updated content"
}'
```

#### Delete a Article

```sh
curl -X DELETE "http://127.0.0.1:8000/api/articles/1" -H "Authorization: Bearer <your_jwt_token>"
```

## Project Structure

```
app/
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── initialize_db.py
├── controller/
│   ├── __init__.py
│   └── article_controller.py
├── model/
│   ├── __init__.py
│   └── article_model.py
├── repository/
│   ├── __init__.py
│   └── article_repository.py
├── service/
│   ├── __init__.py
│   └── article_service.py
├── dto/
│   ├── __init__.py
│   └── article_dto.py
└── main.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Special thanks to the FastAPI and SQLAlchemy communities for their excellent documentation and support.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
