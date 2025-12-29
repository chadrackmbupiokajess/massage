from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactMessage

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    services_list = [
        {
            "name": "Massage Relaxant",
            "description": "Un massage doux pour une relaxation profonde.",
            "duration": "60 min",
            "price": "60€",
            "image": "images/massage_relaxant.jpg"
        },
        {
            "name": "Massage Sportif",
            "description": "Idéal pour la récupération après l'effort.",
            "duration": "45 min",
            "price": "50€",
            "image": "images/massage_sportif.jpg"
        },
        {
            "name": "Massage aux pierres chaudes",
            "description": "Une expérience de détente unique.",
            "duration": "75 min",
            "price": "80€",
            "image": "images/massage_pierres_chaudes.jpg"
        }
    ]
    return render(request, 'main/services.html', {'services': services_list})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return HttpResponseRedirect('/contact?submitted=true')
    return render(request, 'main/contact.html')
