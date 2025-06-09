from django.shortcuts import render

def home(request):
    items = [
        {'id': 1, 'name': 'Котокружка', 'description': 'Керамическая кружка с котиком', 'image_url': '/static/images/photo.png'},
        {'id': 2, 'name': 'Котомайка', 'description': 'Футболка с котиком', 'image_url': '/static/images/photo.png'},
        {'id': 3, 'name': 'Котоплед', 'description': 'Плед с ушками кота', 'image_url': '/static/images/photo.png'},
    ]
    return render(request, 'homepage/home.html', {'items': items})
