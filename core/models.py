import uuid
from django.db import models


class Contact(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # ── Support ───────────────────────────────────────────
    support_tel              = models.CharField(max_length=100, blank=True)
    support_email            = models.CharField(max_length=100, blank=True)
    support_group_whatsapp   = models.CharField(max_length=100, blank=True)
    support_adresse          = models.CharField(max_length=100, blank=True)

    # ── Réseaux sociaux ───────────────────────────────────
    reseau_linkedin  = models.CharField(max_length=100, blank=True)
    reseau_github    = models.CharField(max_length=100, blank=True)
    reseau_facebook  = models.CharField(max_length=100, blank=True)
    reseau_youtube   = models.CharField(max_length=100, blank=True)

    # ── Média ─────────────────────────────────────────────
    image_hero_contact = models.ImageField(
        upload_to='contact/', blank=True, null=True
    )

    # ── Meta ──────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering            = ['-created_at']

    def __str__(self):
        return f"Contact — {self.support_email or str(self.id)}"

    # ── Properties ────────────────────────────────────────
    @property
    def has_social_links(self):
        """Retourne True si au moins un réseau social est renseigné."""
        return any([
            self.reseau_linkedin,
            self.reseau_github,
            self.reseau_facebook,
            self.reseau_youtube,
        ])

    @property
    def social_links(self):
        """Retourne un dict des réseaux sociaux non vides."""
        return {
            k: v for k, v in {
                'linkedin': self.reseau_linkedin,
                'github':   self.reseau_github,
                'facebook': self.reseau_facebook,
                'youtube':  self.reseau_youtube,
            }.items() if v
        }

    @property
    def has_support_info(self):
        """Retourne True si au moins une info de support est renseignée."""
        return any([
            self.support_tel,
            self.support_email,
            self.support_group_whatsapp,
            self.support_adresse,
        ])

    @property
    def whatsapp_url(self):
        """Génère l'URL WhatsApp directe depuis le numéro ou lien."""
        if not self.support_group_whatsapp:
            return ''
        if self.support_group_whatsapp.startswith('http'):
            return self.support_group_whatsapp
        number = self.support_group_whatsapp.replace(' ', '').replace('+', '')
        return f"https://wa.me/{number}"

    @property
    def mailto_url(self):
        """Génère le lien mailto."""
        return f"mailto:{self.support_email}" if self.support_email else ''

