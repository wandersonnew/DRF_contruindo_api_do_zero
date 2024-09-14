from django.urls import path

from . import views

urlpatterns = [
    path("estudantes", views.estudantes, name="estudantes"),
]