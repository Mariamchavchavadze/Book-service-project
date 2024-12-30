# Book Lending Service API

A RESTful API built with Django and Django Rest Framework for managing a book lending service. Users can register, books for lending, and take books from others. The system includes features like authentication, book management, and book filtering.

## Features

- User registration and authentication (JWT tokens).
- CRUD operations on books.
- Ability to filter books by author, genre, and other parameters.
- Manage authors, genres, and book statuses.
- Book location information to know where a book can be picked up.
- Allows users to select who will borrow a book if multiple users are interested.

## Technologies Used

- **Python 3.9+**
- **Django 4.x**
- **Django Rest Framework**
- **PostgreSQL** (configured in settings)
- **Swagger** for API documentation
- **Docker** for containerization

## Setup and Installation

### Prerequisites

- Python 3.9+ installed
- PostgreSQL  set up

### Clone the Repository

Clone the repository to your local machine:

### Swagger
To view the API documentation, navigate to:
http://127.0.0.1:8000/swagger/

### Database
for databse PostgreSQL is used

### Docker containerization 
Docker containerization is working perfectly

```bash
git clone https://github.com/yourusername/book-lending-service.git
cd book-lending-service


