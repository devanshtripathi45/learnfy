from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'slug', 'published_at')
    list_filter = ('type',)
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = { 'slug': ('title',) }
