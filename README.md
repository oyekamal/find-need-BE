# Find Need Backend API

A comprehensive Django REST API backend for a marketplace/classified ads platform with advanced features including user management, posts/listings, chat messaging, push notifications, and location-based services.

## 🚀 Overview

Find Need Backend is a robust, scalable Django-based RESTful API that powers a marketplace application. It provides features for posting and finding classified ads, user authentication with Google OAuth integration, real-time messaging, push notifications via Firebase, and advanced search and filtering capabilities.

### Key Features

- **User Management**: Custom user authentication with email-based login, Google OAuth integration
- **Posts/Listings Management**: CRUD operations for marketplace listings with image uploads
- **Real-time Messaging**: Chat system with file sharing capabilities
- **Push Notifications**: Firebase Cloud Messaging integration for instant notifications
- **Location Services**: Country, city, and region-based filtering
- **Advanced Search**: Filter by categories, conditions, price ranges, and more
- **Boost System**: Featured listings and promotional packages
- **Social Features**: Follow/unfollow users, favorites, reports, and moderation
- **Multi-language Support**: Internationalization ready with language preferences
- **Admin Dashboard**: Comprehensive Django admin interface

## 🏗️ Architecture

### Technology Stack
- **Backend Framework**: Django 4.2.2 + Django REST Framework 3.14.0
- **Database**: PostgreSQL 13 (Production) / SQLite3 (Development)
- **Authentication**: Django AllAuth with Google OAuth2, Token-based authentication
- **Image Processing**: Pillow for image uploads and processing
- **Push Notifications**: Firebase Admin SDK for FCM
- **API Documentation**: drf-yasg (Swagger/OpenAPI)
- **Containerization**: Docker & Docker Compose with Nginx reverse proxy
- **CORS**: Django CORS Headers for cross-origin requests

### Project Structure
```
find-need-BE/
├── app/                          # Main Django application
│   ├── core/                     # Project settings and configuration
│   │   ├── settings.py           # Dynamic settings loader
│   │   ├── local_settings.py     # Development configuration
│   │   ├── docker_settings.py    # Production/Docker configuration
│   │   ├── urls.py              # Main URL configuration
│   │   └── wsgi.py              # WSGI application
│   ├── accountProfile/           # User management app
│   │   ├── models.py            # Custom User, Country, City, Language models
│   │   ├── views.py             # Authentication, profile management views
│   │   ├── serializers.py       # API serializers for user data
│   │   └── signals.py           # User-related signals and hooks
│   ├── post/                     # Posts/listings management app
│   │   ├── models.py            # Post, Category, Images, Boost models
│   │   ├── views.py             # CRUD operations for posts and related data
│   │   ├── serializers.py       # API serializers for post data
│   │   └── management/commands/ # Data population commands
│   ├── static/                   # Static files (CSS, JS, images)
│   ├── templates/                # HTML templates
│   ├── media/                    # User uploaded files
│   ├── requirements.txt          # Python dependencies
│   ├── manage.py                # Django management script
│   ├── Dockerfile.prod          # Production Docker configuration
│   └── entrypoint.sh            # Docker entrypoint script
├── nginx/                        # Nginx reverse proxy configuration
├── docker-compose.yml           # Multi-container Docker setup
└── README.md                    # Project documentation
```

## 📋 Prerequisites

- **Python**: 3.10+
- **PostgreSQL**: 13+ (for production)
- **Docker & Docker Compose**: Latest versions (for containerized deployment)
- **Firebase Project**: For push notifications (optional)
- **Google OAuth Credentials**: For social authentication (optional)

## 🛠️ Installation & Setup

### Option 1: Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/oyekamal/find-need-BE.git
   cd find-need-BE
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   cd app
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory:
   ```env
   # Basic Configuration
   DEBUG=1
   SECRET_KEY=your-secret-key-here
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
   
   # Database (for local development with PostgreSQL)
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE=findneed_db
   SQL_USER=your_db_user
   SQL_PASSWORD=your_db_password
   SQL_HOST=localhost
   SQL_PORT=5432
   DATABASE=postgres
   
   # For SQLite (simpler setup)
   # Just comment out the PostgreSQL settings above
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**:
   ```bash
   python manage.py runserver
   ```

### Option 2: Docker Deployment (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/oyekamal/find-need-BE.git
   cd find-need-BE
   ```

2. **Configure production environment**:
   Create `.env.prod` file:
   ```env
   DEBUG=0
   SECRET_KEY=your-production-secret-key
   DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE=hello_django_prod
   SQL_USER=hello_django
   SQL_PASSWORD=hello_django
   SQL_HOST=db
   SQL_PORT=5432
   DATABASE=postgres
   LOCAL=False
   ```

   Create `.env.prod.db` file:
   ```env
   POSTGRES_USER=hello_django
   POSTGRES_PASSWORD=hello_django
   POSTGRES_DB=hello_django_prod
   ```

3. **Build and start containers**:
   ```bash
   docker-compose up -d --build
   ```

4. **Run migrations in container**:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create superuser in container**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

The application will be available at:
- **API**: http://localhost:8000
- **Admin Interface**: http://localhost:8000/admin
- **API Documentation**: http://localhost:8000/swagger/

## 📊 Database Population

Populate the database with sample data for testing:

```bash
# Local development
python manage.py post_data

# Docker environment
docker-compose exec web python manage.py post_data
```

This command creates:
- **Sample Users**: 5 test users with different roles
- **Geographic Data**: Countries, cities, and regions
- **Categories**: Post categories and subcategories
- **Vehicle Data**: Conditions, transmissions, fuel types, insurance options
- **Sample Posts**: Various types of listings with images
- **Boost Packages**: Premium listing options
- **Social Data**: Follows, favorites, and reports

## 🔧 Configuration

### Firebase Integration (Optional)

For push notifications, configure Firebase in `local_settings.py` or `docker_settings.py`:

```python
FIREBASE_CREDENTIALS = {
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-xxx@your-project.iam.gserviceaccount.com",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    # ... other Firebase config
}
```

### Google OAuth Configuration (Optional)

Configure Google authentication:

```python
GOOGLE_AUTH_CLIENT_ID = "your-client-id.apps.googleusercontent.com"
GOOGLE_AUTH_CLIENT_SECRET = "your-client-secret"
GOOGLE_AUTH_AUTHORIZED_DOMAINS = "yourdomain.com"
```

### Email Configuration

For password reset and notifications:

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "your-email@gmail.com"
EMAIL_HOST_PASSWORD = "your-app-password"
```

## 🚦 API Endpoints

### Authentication
- `POST /dj-rest-auth/login/` - Email/password login
- `POST /dj-rest-auth/logout/` - User logout
- `POST /dj-rest-auth/registration/` - User registration
- `POST /google-login/` - Google OAuth login
- `POST /dj-rest-auth/password/reset/` - Password reset

### User Management
- `GET /api/users/` - List users
- `GET /api/users/{id}/` - User profile
- `PATCH /api/users/{id}/` - Update profile
- `GET /api/languages/` - Available languages
- `POST /api/follow/` - Follow/unfollow users

### Posts & Listings
- `GET /api/posts/` - List posts (with filtering)
- `POST /api/posts/` - Create new post
- `GET /api/posts/{id}/` - Post details
- `PATCH /api/posts/{id}/` - Update post
- `DELETE /api/posts/{id}/` - Delete post

### Categories & Metadata
- `GET /api/categories/` - Post categories
- `GET /api/subcategories/` - Subcategories
- `GET /api/conditions/` - Item conditions
- `GET /api/countries/` - Available countries
- `GET /api/cities/` - Cities by country

### Social Features
- `GET /api/favourites/` - User favorites
- `POST /api/favourites/` - Add to favorites
- `POST /api/reports/` - Report content
- `GET /api/boost-packages/` - Available boost packages

### Messaging
- `GET /api/chat-messages/` - Chat messages
- `POST /api/chat-messages/` - Send message
- `POST /api/notifications/` - Push notifications

### Search & Filtering
Query parameters for posts endpoint:
- `category` - Filter by category ID
- `country` - Filter by country
- `city` - Filter by city
- `min_price`, `max_price` - Price range
- `condition` - Item condition
- `search` - Text search in title/description
- `ordering` - Sort by price, date, etc.

## 📱 Models Overview

### User Management
- **CustomUser**: Extended Django user with profile fields
- **Country/City**: Geographic location data
- **Language**: Multi-language support
- **Follow**: User following relationships

### Content Management
- **Post**: Main listing/ad model with images and metadata
- **Category/Subcategory**: Content categorization
- **Image**: File uploads for posts
- **Condition**: Item conditions (new, used, etc.)

### Business Logic
- **BoostPackage**: Premium listing packages
- **Favourite**: User saved posts
- **Report**: Content moderation system
- **ChatMessage**: Real-time messaging system

## 🔒 Security Features

- **Token Authentication**: Secure API access
- **CORS Configuration**: Cross-origin request handling
- **Input Validation**: Django form validation and DRF serializers
- **Permission Classes**: Role-based access control
- **Rate Limiting**: Built-in Django middleware protection

## 🚀 Deployment

### Production Checklist

1. **Environment Variables**: Set secure production values
2. **Database**: Use PostgreSQL with proper backups
3. **Static Files**: Configure static file serving via Nginx
4. **SSL/HTTPS**: Enable SSL certificates (commented config available)
5. **Monitoring**: Set up logging and monitoring
6. **Security**: Review Django security checklist

### Scaling Considerations

- **Database Optimization**: Add indexes, query optimization
- **Caching**: Implement Redis for session and query caching
- **File Storage**: Use cloud storage (AWS S3, Google Cloud) for media files
- **Load Balancing**: Multiple application instances behind load balancer
- **CDN**: Content delivery network for static assets

## 🧪 Testing

Run the test suite:

```bash
# Local development
python manage.py test

# Docker environment
docker-compose exec web python manage.py test

# Run specific app tests
python manage.py test accountProfile
python manage.py test post
```

## 📝 API Documentation

Interactive API documentation is available at:
- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **JSON Schema**: http://localhost:8000/swagger.json

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is proprietary. All rights reserved.

## 🐛 Troubleshooting

### Common Issues

**Database Connection Issues**:
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Reset database (development only)
python manage.py flush
python manage.py migrate
```

**Docker Issues**:
```bash
# Rebuild containers
docker-compose down
docker-compose up --build

# Check logs
docker-compose logs web
docker-compose logs db
```

**Permission Errors**:
```bash
# Fix file permissions
chmod +x app/entrypoint.sh
sudo chown -R $USER:$USER media/
```

### Development Tips

- Use `DEBUG=True` only in development
- Monitor database queries with Django Debug Toolbar
- Use `django-extensions` for enhanced management commands
- Set up pre-commit hooks for code quality

## 📞 Support

For support and questions:
- **Email**: [Your Email]
- **Issues**: GitHub Issues page
- **Documentation**: Check the `/docs` endpoint for additional API documentation

---

Built with ❤️ using Django REST Framework

## Development Notes

- Use `python manage.py migrate` to apply database migrations
- The application uses PostgreSQL as the database backend
- Static files are served through Nginx in production
- Media files are stored in the `media/` directory
