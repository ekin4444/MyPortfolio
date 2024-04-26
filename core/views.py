# Create your views here.
# views.py
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def single(request):
    # Your view logic here
    return render(request, 'single.html')
def details(request):
    # Your view logic here
    return render(request, 'details.html')
def contact_form(request):
    # Your form processing logic here
    # Assuming the form was sent successfully
    message = "Contact form sent successfully."
    context = {
        "success": True,
        "message": message
    }
    return JsonResponse(context)

def contact(request):
    return None