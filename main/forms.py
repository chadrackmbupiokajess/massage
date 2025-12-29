from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Votre nom complet', 'class': 'py-3 px-4 block w-full shadow-sm focus:ring-green-500 focus:border-green-500 border-gray-300 rounded-md transition-shadow duration-300'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Votre adresse e-mail', 'class': 'py-3 px-4 block w-full shadow-sm focus:ring-green-500 focus:border-green-500 border-gray-300 rounded-md transition-shadow duration-300'}),
            'message': forms.Textarea(attrs={'placeholder': 'Votre message', 'rows': 4, 'class': 'py-3 px-4 block w-full shadow-sm focus:ring-green-500 focus:border-green-500 border border-gray-300 rounded-md transition-shadow duration-300'}),
        }
        labels = {
            'name': 'Nom complet',
            'email': 'Adresse e-mail',
            'message': 'Votre message',
        }
