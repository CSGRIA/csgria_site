from django import forms
from core.models import *

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = [
            'support_tel',
            'support_email',
            'support_group_whatsapp',
            'support_chaine_whatsapp',
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
            'support_chaine_whatsapp':forms.TextInput(attrs={'placeholder': 'whatsapp:https://whatsapp.com/channe/...'}),
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
            'support_chaine_whatsapp': 'Chaine WhatsApp (lien)',
            'support_adresse':        'Adresse',
            'reseau_linkedin':        'LinkedIn',
            'reseau_github':          'GitHub',
            'reseau_facebook':        'Facebook',
            'reseau_youtube':         'YouTube',
            'image_hero_contact':     'Image hero page contact',
        }

class ContactMessageForm(forms.Form):
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

class AproposForm(forms.ModelForm):
    class Meta:
        model   = Apropos
        fields  = ['hero_politique']
        labels  = {'hero_politique':'Image hero'}

class EvenementForm(forms.ModelForm):
    class Meta:
        model   = Evenement
        fields  = ['annee','title','description','ordre']
        widgets = {
            'annee':forms.TextInput(attrs={'placeholder':'2024'}),
            'title':forms.TextInput(attrs={'placeholder':'Titre'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels  = {
            'annee':'Année',
            'title':'Titre',
            'description':'Description',
            'ordre':"Ordre d'affichage",
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = [
            'photo_profile', 'prenom', 'nom',
            'post', 'role', 'ordre', 'bio', 'linkedin',
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
        labels  = {
            'photo_profile':'Photo',
            'prenom':'Prénom',
            'nom':'Nom',
            'post':'Poste',
            'role':'Rôle',
            'ordre':"Ordre d'affichage",
            'bio':'Biographie',
            'linkedin':'LinkedIn',
        }


class CarousselForm(forms.ModelForm):

    class Meta:
        model = Caroussel
        fields = ['bg', 'poster', 'actif', 'ordre']
        widgets = {
            'actif': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'ordre': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': '0',
            }),
            'bg': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'poster': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }
        labels = {
            'bg':     'Arrière-plan',
            'poster': 'Affiche',
            'actif':  'Actif',
            'ordre':  'Ordre d\'affichage',
        }
        help_texts = {
            'bg':     'Image de fond du slide (recommandé : 1920×1080px).',
            'poster': 'Affiche centrale du slide (recommandé : ratio 3/4).',
            'ordre':  'Définit la position du slide dans le carousel.',
        }

    def clean(self):
        cleaned = super().clean()
        bg     = cleaned.get('bg')
        poster = cleaned.get('poster')

        # Au moins une image est requise
        if not bg and not poster:
            raise forms.ValidationError(
                'Veuillez fournir au moins un arrière-plan ou une affiche.'
            )
        return cleaned


class MissionForm(forms.ModelForm):

    class Meta:
        model = Mission
        fields = ['visuel', 'label', 'title', 'description',
                  'is_reverse', 'position', 'actif']
        widgets = {
            'visuel': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'label': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : 01 — Recherche',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de la mission',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description de la mission...',
            }),
            'is_reverse': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'position': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
            }),
            'actif': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
        labels = {
            'visuel':     'Visuel',
            'label':      'Label',
            'title':      'Titre',
            'description':'Description',
            'is_reverse': 'Disposition inversée',
            'position':   'Position',
            'actif':      'Actif',
        }
        help_texts = {
            'visuel':     'Image illustrant la mission (recommandé : 4/3).',
            'label':      'Courte étiquette affichée au-dessus du titre.',
            'is_reverse': 'Cocher pour inverser image et texte.',
            'position':   'Ordre d\'apparition dans la liste.',
        }

