# Create your views here.
# views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from core.models import GeneralSetting, ImageSetting, Skill


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_about = GeneralSetting.objects.get(name='site_about').parameter
    logo = GeneralSetting.objects.get(name='logo').parameter

    # images
    testimonal = ImageSetting.objects.get(name='testimonal').file
    bg = ImageSetting.objects.get(name='bg').file

    # skills
    skills = Skill.objects.all().order_by('order')

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_about': site_about,
        'logo': logo,
        'testimonal': testimonal,
        'bg': bg,
        'skills': skills
    }
    return render(request, 'index.html', context=context)


def single(request):
    # Your view logic here
    return render(request, 'single.html')


def details(request):
    # Your view logic here
    return render(request, 'details.html')


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Send email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Your message has been sent. Thank you!'})
    return JsonResponse({'error': 'Invalid request'})
