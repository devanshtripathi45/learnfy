@echo off
echo ========================================
echo   LEARNIFY - CLEAN SERVER STARTUP
echo ========================================
echo.

echo [1/4] Killing any existing Python processes...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/4] Checking Django configuration...
python manage.py check

echo [3/4] Starting clean Django server...
echo.
echo IMPORTANT: Use ONLY HTTP URLs:
echo   http://127.0.0.1:8000
echo   http://localhost:8000
echo.
echo DO NOT use HTTPS - it will cause errors!
echo.

python manage.py runserver 127.0.0.1:8000 --noreload
