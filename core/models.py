import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _



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
        return any([
            self.reseau_linkedin,
            self.reseau_github,
            self.reseau_facebook,
            self.reseau_youtube,
        ])

    @property
    def social_links(self):
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
        return any([
            self.support_tel,
            self.support_email,
            self.support_group_whatsapp,
            self.support_adresse,
        ])

    @property
    def whatsapp_url(self):
        if not self.support_group_whatsapp:
            return ''
        if self.support_group_whatsapp.startswith('http'):
            return self.support_group_whatsapp
        number = self.support_group_whatsapp.replace(' ', '').replace('+', '')
        return f"https://wa.me/{number}"

    @property
    def mailto_url(self):
        return f"mailto:{self.support_email}" if self.support_email else ''
    
class Apropos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hero_politique = models.ImageField(upload_to='apropos/', blank=True, null=True)

    # accessibles via : apropos.evenements.all() et apropos.profiles.all()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'À propos'
        verbose_name_plural = 'À propos'

    def __str__(self):
        return f"À propos ({self.id})"

    @property
    def chronologie(self):
        return self.evenements.order_by('ordre', 'annee')

    @property
    def gouvernance(self):
        return self.profiles.order_by('ordre', 'nom')

    @property
    def has_hero(self):
        return bool(self.hero_politique)

class Evenement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apropos = models.ForeignKey(
        Apropos,
        on_delete=models.CASCADE,
        related_name='evenements',  
        null=True, blank=True
    )
    annee       = models.CharField(max_length=10)
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    ordre       = models.PositiveIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Événement'
        verbose_name_plural = 'Événements'
        ordering            = ['ordre', 'annee']

    def __str__(self):
        return f"{self.annee} — {self.title}"

class Profile(models.Model):
    ROLE_CHOICES = [
        ('president',      'Président'),
        ('vice_president', 'Vice-Président'),
        ('secretaire',     'Secrétaire'),
        ('membre',         'Membre'),
        ('autre',          'Autre'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apropos       = models.ForeignKey(
        Apropos,
        on_delete=models.CASCADE,
        related_name='profiles',    
        null=True, blank=True
    )
    photo_profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    nom           = models.CharField(max_length=100)
    prenom        = models.CharField(max_length=100)
    post          = models.CharField(max_length=100)
    role          = models.CharField(max_length=30, choices=ROLE_CHOICES, default='membre')
    ordre         = models.PositiveIntegerField(default=0)
    bio           = models.TextField(blank=True)
    linkedin      = models.URLField(blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Profil'
        verbose_name_plural = 'Profils'
        ordering            = ['ordre', 'nom']

    def __str__(self):
        return f"{self.prenom} {self.nom} — {self.post}"

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    @property
    def has_photo(self):
        return bool(self.photo_profile)


class Caroussel(models.Model):
    bg = models.ImageField(
        upload_to='caroussel/bg/',
        blank=True, null=True,
        verbose_name=_('Arrière-plan')
    )
    poster = models.ImageField(
        upload_to='caroussel/poster/',
        blank=True, null=True,
        verbose_name=_('Affiche')
    )
    actif = models.BooleanField(
        default=False,
        verbose_name=_('Actif')
    )
    ordre = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('Ordre d\'affichage'),
        help_text=_('Numéro d\'ordre dans le carousel (0 = premier)')
    )
    date_creat = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date de création')
    )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Dernière modification')
    )

    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')
        ordering = ['ordre', 'date_creat']

    def __str__(self):
        statut = 'actif' if self.actif else 'inactif'
        return f'Carousel #{self.pk} — {statut}'

    @property
    def bg_url(self):
        return self.bg.url if self.bg else None

    @property
    def poster_url(self):
        return self.poster.url if self.poster else None

    @property
    def has_bg(self):
        return bool(self.bg)

    @property
    def has_poster(self):
        return bool(self.poster)


class Mission(models.Model):
    visuel = models.ImageField(
        upload_to='mission/visuel/',
        blank=True, null=True,
        verbose_name=_('Visuel')
    )
    label = models.CharField(
        max_length=100,
        verbose_name=_('Label'),
        help_text=_('Ex : 01 — Recherche')
    )
    title = models.CharField(
        max_length=150,
        verbose_name=_('Titre')
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    is_reverse = models.BooleanField(
        default=False,
        verbose_name=_('Inversé'),
        help_text=_('Affiche l\'image à gauche et le texte à droite')
    )
    position = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('Position'),
        help_text=_('Ordre d\'affichage dans la section Missions')
    )
    actif = models.BooleanField(
        default=True,
        verbose_name=_('Actif')
    )
    date_creat = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date de création')
    )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Dernière modification')
    )

    class Meta:
        verbose_name = _('Mission')
        verbose_name_plural = _('Missions')
        ordering = ['position', 'date_creat']

    def __str__(self):
        return f'{self.label} — {self.title}'

    @property
    def visuel_url(self):
        return self.visuel.url if self.visuel else None

    @property
    def has_visuel(self):
        return bool(self.visuel)


