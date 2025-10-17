from django.shortcuts import render, get_object_or_404
from .models import Item


def blog_index(request):
    items = Item.objects.filter(type=Item.TYPE_BLOG)
    return render(request, 'blog/index.html', { 'items': items })


def blog_detail(request, slug):
    item = get_object_or_404(Item, type=Item.TYPE_BLOG, slug=slug)
    return render(request, 'blog/detail.html', { 'item': item })
