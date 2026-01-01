from django import forms
from .models import Reservation, ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'
    attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}

class TimeInput(forms.TimeInput):
    input_type = 'time'
    attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'name', 'phone', 'email', 
            'country', 'city', 'address',
            'date', 'time', 'service'
        ]
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
            'name': forms.TextInput(attrs={'placeholder': 'Votre nom complet', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Votre numéro de téléphone', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Votre adresse email', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'country': forms.TextInput(attrs={'placeholder': 'Pays', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'city': forms.TextInput(attrs={'placeholder': 'Ville', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'address': forms.Textarea(attrs={'placeholder': 'Votre adresse complète', 'rows': 3, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'service': forms.HiddenInput(), # Le service sera pré-rempli et caché
        }
        labels = {
            'name': 'Nom complet',
            'phone': 'Téléphone',
            'email': 'Email',
            'country': 'Pays',
            'city': 'Ville',
            'address': 'Adresse',
            'date': 'Date du rendez-vous',
            'time': 'Heure du rendez-vous',
        }
