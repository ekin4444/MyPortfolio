# urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('single.html', views.single, name='single'),
    path('details.html', views.details, name='details'),
    path('contact_form/', views.contact_form, name='contact_form'),
    # Add other URL patterns for blog and portfolio if needed
]
