from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import Service, Reservation, ContactMessage, CarouselSlide, HomePageContent, Testimonial, AboutPageContent, Commitment, ContactPageContent
from .forms import ContactForm, ReservationForm

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
            contact_message = form.save()

            # Send notification email to the admin
            admin_subject = f"Nouveau message de {contact_message.name}"
            admin_message = (
                f"Vous avez reçu un nouveau message de la part de {contact_message.name} ({contact_message.email}).\n\n"
                f"Message :\n{contact_message.message}"
            )
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL]
            )

            return redirect('/contact?submitted=true')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {
        'form': form,
        'content': contact_content,
        'submitted': request.GET.get('submitted', False)
    })

def reservation_view(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            
            # Send confirmation email to the client
            client_subject = f"Confirmation de votre réservation pour {reservation.service.name}"
            client_message = render_to_string('emails/client_confirmation.txt', {'reservation': reservation})
            send_mail(client_subject, client_message, settings.DEFAULT_FROM_EMAIL, [reservation.email])

            # Send notification email to the admin
            admin_subject = f"Nouvelle réservation de {reservation.name} pour {reservation.service.name}"
            admin_message = render_to_string('emails/admin_notification.txt', {'reservation': reservation})
            send_mail(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

            return redirect('reservation_confirmation', reservation_id=reservation.id)
    else:
        form = ReservationForm(initial={'service': service})

    return render(request, 'main/reservation_form.html', {
        'form': form,
        'service': service
    })

def reservation_confirmation_view(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'main/reservation_confirmation.html', {'reservation': reservation})
