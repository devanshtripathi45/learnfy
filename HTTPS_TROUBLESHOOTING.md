# HTTPS Error Troubleshooting Guide

## 🚨 Problem
You're getting constant HTTPS connection attempts to your Django development server, causing errors like:
```
ERROR You're accessing the development server over HTTPS, but it only supports HTTP.
```

## 🔍 Root Causes
The HTTPS connection attempts are coming from external sources, NOT your Django project:
1. **Browser Extensions** (HTTPS Everywhere, security extensions)
2. **Antivirus Software** (scanning web traffic)
3. **Browser Cache** (cached HTTPS redirects)
4. **Development Tools** (VS Code extensions, Postman, etc.)
5. **System Network Settings** (Windows security features)

## ✅ Solutions

### 1. **Use the New Startup Scripts**
```bash
# Windows Batch
start_http_only.bat

# PowerShell
.\start_http_only.ps1
```

### 2. **Clear Browser Cache Completely**
- **Chrome**: Ctrl+Shift+Delete → Select "All time" → Clear data
- **Firefox**: Ctrl+Shift+Delete → Select "Everything" → Clear Now
- **Edge**: Ctrl+Shift+Delete → Select "All time" → Clear

### 3. **Use Incognito/Private Mode**
- **Chrome**: Ctrl+Shift+N
- **Firefox**: Ctrl+Shift+P
- **Edge**: Ctrl+Shift+N

### 4. **Disable Browser Extensions**
- Temporarily disable all extensions
- Especially disable "HTTPS Everywhere" or similar extensions

### 5. **Check Antivirus Settings**
- Disable web scanning temporarily
- Add your localhost to exceptions

### 6. **Use Different Port**
If issues persist, try a different port:
```bash
python manage.py runserver 127.0.0.1:8001 --noreload
```

### 7. **Check for Background Processes**
```bash
# Check what's running on port 8000
netstat -ano | findstr :8000

# Kill any conflicting processes
taskkill /F /PID <process_id>
```

## 🎯 **Quick Fix Steps**

1. **Stop current server** (Ctrl+C)
2. **Run the new startup script**: `start_http_only.bat`
3. **Open browser in incognito mode**
4. **Navigate to**: `http://127.0.0.1:8000` (NOT https)
5. **If still getting errors, try port 8001**

## 📝 **What We've Fixed**

✅ Removed all HTTPS references from templates
✅ Updated Django settings to force HTTP-only mode
✅ Created startup scripts with environment variables
✅ Added comprehensive troubleshooting guide

## 🚀 **Expected Result**
After following these steps, you should see:
- Clean server startup without HTTPS errors
- Website loads properly at `http://127.0.0.1:8000`
- No more "HTTPS but it only supports HTTP" errors

## 🔧 **If Problems Persist**
The HTTPS connection attempts are coming from external sources. The Django server itself is correctly configured for HTTP-only mode.
