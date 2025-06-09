from django.shortcuts import render
from catalog.models import Item

def home(request):
    items = Item.objects.filter(is_published=True).select_related('category').prefetch_related('tags')
    return render(request, 'homepage/home.html', {'items': items})
