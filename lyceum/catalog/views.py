import django.http
from django.shortcuts import render, get_object_or_404
from .models import Item


def main_page(request):
    items = (
        Item.objects.filter(is_published=True, is_on_main=True)
        .select_related("category")
        .prefetch_related("tags")
        .only("name", "description", "category__name")
        .order_by("name")
    )
    return render(request, 'catalog/main.html', {'items': items})


def item_list(request):
    items = Item.objects.filter(is_published=True)
    return render(request, 'catalog/list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'catalog/detail.html', {'item': item})
