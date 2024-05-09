# urls.py

from django.urls import path
from .views import index, contact, contact_form, neuro_details, eco_details, seat_details

urlpatterns = [
    path('', index, name='index'),
    path('neuro_details.html', neuro_details, name='neuro_details'),
    path('eco_details.html', eco_details, name='eco_details'),
    path('seat_details.html', seat_details, name='seat_details'),
    path('index.html', contact_form, name='contact_form'),
    # Add other URL patterns for blog and portfolio if needed
]
