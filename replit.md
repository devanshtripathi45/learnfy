# Learnify - Learning Platform

## Overview
Learnify is a Django-based learning platform that provides courses and blog content. It features user authentication, course management, blog posts, and a search functionality.

## Project Structure
- `learnfy/` - Django project settings and main URLs
- `accounts/` - User authentication and contact functionality  
- `courses/` - Course management application
- `blog/` - Blog posts management
- `templates/` - HTML templates
- `static/` - CSS, images, and static assets
- `db.sqlite3` - SQLite database (development)

## Recent Changes (October 20, 2025)
- ✅ Fixed search functionality by adding missing `/search/` URL endpoint
- ✅ Created `search_view()` function to handle search queries
- ✅ Added `search_results.html` template to display results
- ✅ Configured Django settings for Replit environment (`ALLOWED_HOSTS = ['*']`)
- ✅ Fixed requirements.txt encoding issues
- ✅ Ran migrations and collected static files
- ✅ Configured workflow to run Django dev server on port 5000

## Key Features
- **Course Management**: Browse and view detailed course information
- **Blog Posts**: Read educational blog content
- **Search**: Search across courses and blog posts by title, description, or content
- **User Authentication**: Login and signup functionality
- **Contact Form**: Users can send messages to administrators
- **Responsive Design**: Bootstrap-based responsive UI

## Environment Setup
- **Python Version**: 3.11.9
- **Framework**: Django 5.2.7
- **Database**: SQLite (development)
- **Server**: Django development server on 0.0.0.0:5000

## Dependencies
- Django
- gunicorn (production server)
- psycopg2-binary (PostgreSQL support)
- dj-database-url (database configuration)
- whitenoise (static files)
- python-dotenv (environment variables)
- Pillow (image processing)

## Running the Project
The project is configured to run automatically through the Server workflow:
```bash
python manage.py runserver 0.0.0.0:5000
```

## Search Functionality Fix
**Problem**: The search form in the navbar was submitting to `/search/` but no URL pattern existed, causing 404 errors.

**Solution**: 
1. Added `search_view()` function in `learnfy/urls.py` that:
   - Gets the search query from `request.GET.get('q')`
   - Uses Django Q objects to search across title, description, and content fields
   - Returns results for both courses and blog posts
2. Created `search_results.html` template to display search results with proper styling
3. Added `/search/` URL pattern to urlpatterns

## Important Configuration for Replit
- `ALLOWED_HOSTS = ['*']` in DEBUG mode (required for Replit's proxy)
- `X_FRAME_OPTIONS = 'SAMEORIGIN'` (allows iframe embedding)
- Server binds to `0.0.0.0:5000` (required for external access)
- All HTTPS/SSL settings disabled in DEBUG mode

## Admin Access
Create a superuser to access the admin panel at `/admin/`:
```bash
python manage.py createsuperuser
```
