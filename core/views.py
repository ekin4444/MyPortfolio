# Create your views here.
# views.py
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from contact.models import Message
from core.models import GeneralSetting, Skill, Experience, Education, SocialMedia, Language, Reference, Project


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_about = GeneralSetting.objects.get(name='site_about').parameter
    logo = GeneralSetting.objects.get(name='logo').parameter

    # skills
    skills = Skill.objects.all().order_by('-percentage')
    # -percentage yazarak websitesindeki sırayı yüzdeye göre değiştirdik

    experiences = Experience.objects.all()
    educations = Education.objects.all()
    social_medias = SocialMedia.objects.all()
    languages = Language.objects.all()
    references = Reference.objects.all()
    projects = Project.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_about': site_about,
        'logo': logo,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'social_medias': social_medias,
        'languages': languages,
        'references': references,
        'projects': projects
    }
    return render(request, 'index.html', context=context)


def neuro_details(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    logo = GeneralSetting.objects.get(name='logo').parameter

    context = {
        'site_title': site_title,
        'logo': logo,
    }
    # Your view logic here
    return render(request, 'neuro_details.html', context=context)


def eco_details(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    logo = GeneralSetting.objects.get(name='logo').parameter

    context = {
        'site_title': site_title,
        'logo': logo,
    }
    return render(request, 'eco_details.html', context=context)


def seat_details(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    logo = GeneralSetting.objects.get(name='logo').parameter

    context = {
        'site_title': site_title,
        'logo': logo,
    }
    return render(request, 'seat_details.html', context=context)


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

        print("Form succesfully submitted")
        return HttpResponseRedirect(reverse('index'))
    else:

        print("Form not submitted")
        return render(request, 'index.html', {"message_name": "hata"})
