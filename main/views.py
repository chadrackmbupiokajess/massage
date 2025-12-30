from django.shortcuts import render, redirect
from .models import Service, ContactMessage, CarouselSlide, HomePageContent, Testimonial, AboutPageContent, Commitment, ContactPageContent
from .forms import ContactForm

def home(request):
    featured_services = Service.objects.all()[:3]
    slides = CarouselSlide.objects.all()
    home_content = HomePageContent.load()
    testimonials = Testimonial.objects.filter(is_visible=True)

    return render(request, 'main/home.html', {
        'featured_services': featured_services,
        'slides': slides,
        'home_content': home_content,
        'testimonials': testimonials,
    })

def about(request):
    about_content = AboutPageContent.load()
    commitments = Commitment.objects.all()
    return render(request, 'main/about.html', {
        'content': about_content,
        'commitments': commitments
    })

def services(request):
    services_list = Service.objects.all()
    return render(request, 'main/services.html', {'services': services_list})

def contact(request):
    contact_content = ContactPageContent.load()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact?submitted=true')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {
        'form': form,
        'content': contact_content,
        'submitted': request.GET.get('submitted', False)
    })
