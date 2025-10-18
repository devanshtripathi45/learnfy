@echo off
echo ========================================
echo Learnify - HTTP Only Server Startup
echo ========================================
echo.

echo Killing any existing Python processes...
taskkill /F /IM python.exe > nul 2>&1
echo.

echo Setting environment variables to force HTTP...
set DJANGO_SETTINGS_MODULE=learnify.settings
set DEBUG=True
set ALLOWED_HOSTS=*
set SECURE_SSL_REDIRECT=False
set CSRF_COOKIE_SECURE=False
set SESSION_COOKIE_SECURE=False
set SECURE_HSTS_SECONDS=0
set SECURE_HSTS_INCLUDE_SUBDOMAINS=False
set SECURE_HSTS_PRELOAD=False
set SECURE_PROXY_SSL_HEADER=None
set SECURE_REFERRER_POLICY=None
set SECURE_CROSS_ORIGIN_OPENER_POLICY=None

echo.
echo IMPORTANT: Clear your browser cache or use incognito mode!
echo.
echo Starting Django server on HTTP only...
echo Server will be available at: http://127.0.0.1:8000
echo.

python manage.py runserver 127.0.0.1:8000 --noreload
