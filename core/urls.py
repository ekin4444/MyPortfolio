# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns for blog and portfolio if needed
]
