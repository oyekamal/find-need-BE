# Find Need Backend

A Django-based backend application for managing posts, categories, and related data.

## Prerequisites

- Python 3.10
- PostgreSQL
- Docker and Docker Compose (for containerized deployment)

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/oyekamal/find-need-BE/
cd find-need-BE
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd app
pip install -r requirements.txt
```

4. Create `.env` file in the root directory with the following variables:
```env
DEBUG=1
SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=your_db_name
SQL_USER=your_db_user
SQL_PASSWORD=your_db_password
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

## Docker Deployment

1. Create `.env.prod` and `.env.prod.db` files with appropriate production settings.

2. Build and run the containers:
```bash
docker-compose up -d --build
```

The application will be available at:
- Main application: http://localhost:8000
- Adminer (Database management): http://localhost:8080

## Database Population

To populate the database with sample data, run:
```bash
python manage.py post_data
```

This command will create:
- Sample users
- Categories and subcategories
- Post types
- Various vehicle-related data
- Sample posts with images
- Favorites and reports
- Boost packages and requests

## Available API Endpoints

The application provides endpoints for:
- Posts management
- Categories and subcategories
- User favorites
- Reports
- Boost packages and requests
- Image management
- Various vehicle-related data (conditions, transmissions, etc.)

## Admin Interface

Access the Django admin interface at `/admin` to manage:
- Users
- Posts
- Categories
- Images
- All other related models

## Project Structure

- `app/` - Main Django application
- `post/` - Main application module containing models and views
- `nginx/` - Nginx configuration for production
- `docker-compose.yml` - Docker composition configuration
- `Dockerfile.prod` - Production Docker configuration

## Development Notes

- Use `python manage.py migrate` to apply database migrations
- The application uses PostgreSQL as the database backend
- Static files are served through Nginx in production
- Media files are stored in the `media/` directory
