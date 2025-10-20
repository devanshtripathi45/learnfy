"""
URL configuration for learnify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home_view(request):
    # Use unified Item model for latest content
    from blog.models import Item
    posts = Item.objects.filter(type=Item.TYPE_BLOG)[:2]
    courses = Item.objects.filter(type=Item.TYPE_COURSE)[:2]
    return render(request, 'home.html', { 'posts': posts, 'courses': courses })


def simple_health_check(request):
    """Simple health check for Railway root path"""
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok', 'message': 'Server is running'})


def about_view(request):
    from accounts.models import About
    about = About.objects.first()
    return render(request, 'about.html', { 'about': about })


def contact_view(request):
    from accounts.forms import ContactForm
    from django.contrib import messages
    from django.core.mail import send_mail

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send notification email (console backend in dev)
            try:
                send_mail(
                    subject=f"New contact from {contact.name}",
                    message=contact.message,
                    from_email=None,
                    recipient_list=["admin@learnify.example"],
                    fail_silently=False,
                )
            except Exception:
                # Don't break user flow if email fails; it's development console backend
                pass
            messages.success(request, 'Thank you — your message has been sent.')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', { 'form': form })


def health_check(request):
    """Simple health check endpoint for deployment platforms"""
    from django.http import JsonResponse
    from django.db import connection
    from django.core.cache import cache
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        # Test cache (if available)
        cache.set('health_check', 'ok', 10)
        cache.get('health_check')
        
        return JsonResponse({
            'status': 'healthy', 
            'message': 'Learnify is running!',
            'database': 'connected',
            'cache': 'working'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'message': f'Error: {str(e)}'
        }, status=500)


def search_view(request):
    """Search functionality for courses and blog posts"""
    from blog.models import Item
    from django.db.models import Q
    
    query = request.GET.get('q', '').strip()
    results = []
    
    if query:
        # Search in both courses and blog posts
        results = Item.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    
    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('search/', search_view, name='search'),
    path('health/', health_check, name='health'),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
