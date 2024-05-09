# Create your views here.
# views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from contact.models import Message
from core.models import GeneralSetting, Skill, Experience


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_about = GeneralSetting.objects.get(name='site_about').parameter
    logo = GeneralSetting.objects.get(name='logo').parameter

    # skills
    skills = Skill.objects.all().order_by('order')

    experiences = Experience.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_about': site_about,
        'logo': logo,
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'index.html', context=context)


def single(request):
    # Your view logic here
    return render(request, 'single.html')


def details(request):
    # Your view logic here
    return render(request, 'details.html')


def contact(request):
    return render(request, 'index.html')


def contact_form(request):
    print("hello from contact_from function")
    if request.method == 'POST':
        nameText = request.POST['name']
        emailText = request.POST['email']
        subjectText = request.POST['subject']
        messageText = request.POST['message']
        print("hello from contact_from if state")

        send_mail(
            "Message From :" + subjectText,
            f"Name: {nameText}\nEmail: {emailText}\n\n{messageText}",  # E-posta gövdesi
            'your-email@example.com',  # Gönderen e-posta adresi
            ['ekinfilizatass@gmail.com'],  # Alıcı e-posta adresi
        )

        print("if worked")
        return render(request, 'index.html', {"message_name": nameText})
    else:

        print("else worked")
        return render(request, 'index.html', {"message_name": "sa"})
