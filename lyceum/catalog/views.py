import django.http
from django.shortcuts import render


def item_list(request):
    return django.http.HttpResponse("Список элементов")


def item_detail(request, pk):
    return django.http.HttpResponse(f"Подробно элемент {pk}")

def item_detail(request, item_id):
    return render(request, 'catalog/detail.html', {'item_id': item_id})

