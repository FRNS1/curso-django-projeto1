from django.http import HttpResponse
from django.urls import path

from .views import *

app_name = "recipes"

urlpatterns = [
    path('', home),  # home page
    path('recipe/<int:id>/', recipe)
]
