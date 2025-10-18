Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Learnify - HTTP Only Server Startup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Killing any existing Python processes..." -ForegroundColor Yellow
taskkill /F /IM python.exe -ErrorAction SilentlyContinue | Out-Null
Write-Host ""

Write-Host "Setting environment variables to force HTTP..." -ForegroundColor Green
$env:DJANGO_SETTINGS_MODULE = "learnify.settings"
$env:DEBUG = "True"
$env:ALLOWED_HOSTS = "*"
$env:SECURE_SSL_REDIRECT = "False"
$env:CSRF_COOKIE_SECURE = "False"
$env:SESSION_COOKIE_SECURE = "False"
$env:SECURE_HSTS_SECONDS = "0"
$env:SECURE_HSTS_INCLUDE_SUBDOMAINS = "False"
$env:SECURE_HSTS_PRELOAD = "False"
$env:SECURE_PROXY_SSL_HEADER = "None"
$env:SECURE_REFERRER_POLICY = "None"
$env:SECURE_CROSS_ORIGIN_OPENER_POLICY = "None"

Write-Host ""
Write-Host "IMPORTANT: Clear your browser cache or use incognito mode!" -ForegroundColor Red
Write-Host ""
Write-Host "Starting Django server on HTTP only..." -ForegroundColor Green
Write-Host "Server will be available at: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host ""

python manage.py runserver 127.0.0.1:8000 --noreload
