from django import forms
from .models import *

class ContactInfoForm(forms.ModelForm):
    """Formulaire admin — modifier les infos de contact."""
    class Meta:
        model  = Contact
        fields = [
            'support_tel',
            'support_email',
            'support_group_whatsapp',
            'support_adresse',
            'reseau_linkedin',
            'reseau_github',
            'reseau_facebook',
            'reseau_youtube',
            'image_hero_contact',
        ]
        widgets = {
            'support_tel':            forms.TextInput(attrs={'placeholder': '+212 6 00 00 00 00'}),
            'support_email':          forms.EmailInput(attrs={'placeholder': 'contact@example.com'}),
            'support_group_whatsapp': forms.TextInput(attrs={'placeholder': 'https://chat.whatsapp.com/... ou +212...'}),
            'support_adresse':        forms.TextInput(attrs={'placeholder': 'Adresse complète'}),
            'reseau_linkedin':        forms.URLInput(attrs={'placeholder': 'https://linkedin.com/in/...'}),
            'reseau_github':          forms.URLInput(attrs={'placeholder': 'https://github.com/...'}),
            'reseau_facebook':        forms.URLInput(attrs={'placeholder': 'https://facebook.com/...'}),
            'reseau_youtube':         forms.URLInput(attrs={'placeholder': 'https://youtube.com/@...'}),
        }
        labels = {
            'support_tel':            'Téléphone',
            'support_email':          'Email de support',
            'support_group_whatsapp': 'WhatsApp (lien ou numéro)',
            'support_adresse':        'Adresse',
            'reseau_linkedin':        'LinkedIn',
            'reseau_github':          'GitHub',
            'reseau_facebook':        'Facebook',
            'reseau_youtube':         'YouTube',
            'image_hero_contact':     'Image hero page contact',
        }


class ContactMessageForm(forms.Form):
    """Formulaire public — envoyer un message de contact."""
    nom     = forms.CharField(
        max_length=100,
        label='Nom complet',
        widget=forms.TextInput(attrs={'placeholder': 'Votre nom'})
    )
    email   = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'votre@email.com'})
    )
    sujet   = forms.CharField(
        max_length=200,
        label='Sujet',
        widget=forms.TextInput(attrs={'placeholder': 'Objet de votre message'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Votre message…'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise forms.ValidationError("Le message doit contenir au moins 10 caractères.")
        return message