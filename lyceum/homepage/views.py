from django.shortcuts import render
from catalog.models import Item
from django.http import HttpResponseNotAllowed, HttpResponse
from .forms import EchoForm

def home(request):
    items = Item.objects.filter(is_published=True).select_related('category').prefetch_related('tags')
    return render(request, 'homepage/home.html', {'items': items})


def echo_view(request):
    return render(request, 'homepage/echo.html', {'form': EchoForm()})


def echo_submit(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    form = EchoForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        return HttpResponse(text, content_type='text/plain')
    return HttpResponse("Неверные данные", status=400)
