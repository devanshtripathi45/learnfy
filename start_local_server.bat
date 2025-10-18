@echo off
echo Starting Django development server...
echo.
echo IMPORTANT: Use HTTP (not HTTPS) to access your site:
echo   http://127.0.0.1:8000
echo   http://localhost:8000
echo.
echo If your browser tries to use HTTPS, clear your browser cache or use incognito mode.
echo.
python manage.py runserver 127.0.0.1:8000
