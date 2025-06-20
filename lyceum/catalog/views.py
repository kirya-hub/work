from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Item

def main_page(request):
    items = (
        Item.objects.filter(is_published=True, is_on_main=True)
        .select_related("category")
        .prefetch_related("tags")
        .only("name", "text", "category__name")
        .order_by("name")
    )
    return render(request, 'catalog/main.html', {'items': items})


def item_list(request):
    items = (
        Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related("tags")
        .only("name", "text", "category__name")
        .order_by("category__name", "name")
    )
    return render(request, 'catalog/list.html', {'items': items})


def item_detail(request, pk):
    item = (
        Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related("tags", "images")  # images — это related_name для дополнительных фото
        .only("name", "text", "main_image", "category__name")
        .filter(pk=pk)
        .first()
    )

    if not item:
        raise Http404("Товар не найден или не опубликован")

    return render(request, 'catalog/detail.html', {'item': item})
