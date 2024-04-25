# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single.html', views.single, name='single'),
    path('details.html', views.details, name='details'),
    # Add other URL patterns for blog and portfolio if needed
]
