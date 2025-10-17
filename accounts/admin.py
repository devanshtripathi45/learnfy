from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name', 'about_text')

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_at')
	readonly_fields = ('created_at',)
	search_fields = ('name', 'email', 'message')
