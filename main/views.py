from django.shortcuts import render, redirect
from .models import Service, ContactMessage, CarouselSlide
from .forms import ContactForm

def home(request):
    featured_services = Service.objects.all()[:3]
    slides = CarouselSlide.objects.all()
    return render(request, 'main/home.html', {
        'featured_services': featured_services,
        'slides': slides
    })

def about(request):
    return render(request, 'main/about.html')

def services(request):
    services_list = Service.objects.all()
    return render(request, 'main/services.html', {'services': services_list})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact?submitted=true')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
