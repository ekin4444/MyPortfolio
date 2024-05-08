# urls.py

from django.urls import path
from .views import index, contact, contact_form, single, details

urlpatterns = [
    path('', index, name='index'),
    path('single.html', single, name='single'),
    path('details.html', details, name='details'),
    path('index.html', contact_form, name='contact_form'),
    # Add other URL patterns for blog and portfolio if needed
]
