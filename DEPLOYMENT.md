# Deployment Guide

## Environment Variables

Set these environment variables in your production environment:

```bash
# Django Settings
DJANGO_SECRET_KEY=your-very-long-random-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (for production, use PostgreSQL)
DATABASE_URL=postgresql://username:password@localhost:5432/learnify_db

# Email Settings (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

## Deployment Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   - Copy the environment variables above
   - Set them in your production environment

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server:**
   ```bash
   gunicorn learnify.wsgi
   ```

## For Heroku Deployment

1. Create a Heroku app
2. Set environment variables in Heroku dashboard
3. Deploy using Git:
   ```bash
   git push heroku main
   ```

## For VPS/Server Deployment

1. Install Python 3.11+
2. Install PostgreSQL
3. Set up a reverse proxy (Nginx)
4. Use systemd to manage the Gunicorn process
5. Set up SSL certificates

## Security Checklist

- [ ] Set a strong SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use HTTPS in production
- [ ] Set up proper database credentials
- [ ] Configure email settings
- [ ] Set up logging
- [ ] Regular backups
