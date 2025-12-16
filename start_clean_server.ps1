Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   LEARNIFY - CLEAN SERVER STARTUP" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/4] Killing any existing Python processes..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

Write-Host "[2/4] Checking Django configuration..." -ForegroundColor Yellow
python manage.py check

Write-Host "[3/4] Starting clean Django server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "IMPORTANT: Use ONLY HTTP URLs:" -ForegroundColor Green
Write-Host "  http://127.0.0.1:8000" -ForegroundColor White
Write-Host "  http://localhost:8000" -ForegroundColor White
Write-Host ""
Write-Host "DO NOT use HTTPS - it will cause errors!" -ForegroundColor Red
Write-Host ""

python manage.py runserver 127.0.0.1:8000 --noreload



