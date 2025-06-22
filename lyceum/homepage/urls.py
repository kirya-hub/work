from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.home, name="home"),
    path('echo/', views.echo_view, name='echo'),
    path('echo/submit/', views.echo_submit, name='echo_submit'),
]
