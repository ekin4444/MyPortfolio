# Create your views here.
# views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def single(request):
    # Your view logic here
    return render(request, 'single.html')
def details(request):
    # Your view logic here
    return render(request, 'details.html')