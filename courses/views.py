from django.shortcuts import render, get_object_or_404
from blog.models import Item


def course_list(request):
    items = Item.objects.filter(type=Item.TYPE_COURSE)
    return render(request, 'courses/index.html', { 'items': items })


def course_detail(request, slug):
    item = get_object_or_404(Item, type=Item.TYPE_COURSE, slug=slug)
    return render(request, 'courses/detail.html', { 'item': item })
