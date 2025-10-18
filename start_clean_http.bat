@echo off
echo ========================================
echo Learnify - Clean HTTP Server Startup
echo ========================================
echo.

echo Killing any existing Python processes...
taskkill /F /IM python.exe > nul 2>&1
echo.

echo Clearing browser cache instructions:
echo 1. Press Ctrl+Shift+Delete in your browser
echo 2. Select "All time" and clear cache
echo 3. Or use incognito/private mode
echo.

echo Starting Django development server on HTTP only...
echo Server will be available at: http://127.0.0.1:8000
echo.

python manage.py runserver 127.0.0.1:8000 --noreload
