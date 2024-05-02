from django.http import JsonResponse
from django.shortcuts import render
from .models import Message


def contact_form(request):
    if request.method.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message),

        success = True
        message = 'Contact form sent successfully'
    else:
        success = False
        message = 'Request method is not valid.'
    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)


def contact(request):
    return render(request, 'contact.html')
