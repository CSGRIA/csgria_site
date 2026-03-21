from django.contrib import admin
from django.utils.html import format_html
from .models import *

class EvenementInline(admin.TabularInline):
    model  = Evenement
    extra  = 1
    fields = ('annee', 'title', 'description', 'ordre')
    ordering = ('ordre', 'annee')

class ProfileInline(admin.TabularInline):
    model  = Profile
    extra  = 1
    fields = ('photo_profile', 'prenom', 'nom', 'post', 'role', 'ordre')
    ordering = ('ordre',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    # ── Liste ─────────────────────────────────────────────
    list_display  = ('support_email', 'support_tel', 'support_adresse', 'has_social_links', 'updated_at')
    list_filter   = ('created_at', 'updated_at')
    search_fields = ('support_email', 'support_tel', 'support_adresse')
    readonly_fields = ('id', 'created_at', 'updated_at', 'whatsapp_url', 'mailto_url')
    ordering      = ('-created_at',)

    # ── Détail ────────────────────────────────────────────
    fieldsets = (
        ('Identifiant', {
            'fields': ('id',),
            'classes': ('collapse',),
        }),
        ('Support', {
            'fields': (
                'support_tel',
                'support_email',
                'mailto_url',
                'support_group_whatsapp',
                'whatsapp_url',
                'support_adresse',
            ),
        }),
        ('Réseaux sociaux', {
            'fields': (
                'reseau_linkedin',
                'reseau_github',
                'reseau_facebook',
                'reseau_youtube',
            ),
        }),
        ('Média', {
            'fields': ('image_hero_contact',),
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # ── Properties  ─────────
    @admin.display(boolean=True, description='Réseaux sociaux')
    def has_social_links(self, obj):
        return obj.has_social_links
    
@admin.register(Apropos)
class AproposAdmin(admin.ModelAdmin):
    list_display    = ('__str__', 'has_hero', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    inlines         = [EvenementInline, ProfileInline]
    fieldsets       = (
        ('Identifiant', {
            'fields': ('id',),
            'classes': ('collapse',),
        }),
        ('Contenu', {
            'fields': ('hero_politique',),
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(boolean=True, description='Image hero')
    def has_hero(self, obj):
        return obj.has_hero

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display    = ('annee', 'title', 'ordre', 'updated_at')
    list_editable   = ('ordre',)
    search_fields   = ('title', 'annee')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering        = ('ordre', 'annee')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display    = ('nom_complet', 'post', 'role', 'ordre', 'has_photo')
    list_editable   = ('ordre',)
    list_filter     = ('role',)
    search_fields   = ('nom', 'prenom', 'post')
    readonly_fields = ('id', 'nom_complet', 'created_at', 'updated_at')
    ordering        = ('ordre', 'nom')

    @admin.display(boolean=True, description='Photo')
    def has_photo(self, obj):
        return obj.has_photo

@admin.register(Caroussel)
class CarousselAdmin(admin.ModelAdmin):

    list_display  = ('id', 'apercu_bg', 'apercu_poster', 'actif', 'ordre',
                     'date_creat', 'date_update')
    list_display_links = ('id', 'apercu_bg')
    list_editable = ('actif', 'ordre')
    list_filter   = ('actif',)
    ordering      = ('ordre', 'date_creat')
    readonly_fields = ('date_creat', 'date_update', 'apercu_bg', 'apercu_poster')

    fieldsets = (
        ('Médias', {
            'fields': (
                ('bg', 'apercu_bg'),
                ('poster', 'apercu_poster'),
            ),
        }),
        ('Paramètres', {
            'fields': ('actif', 'ordre'),
        }),
        ('Horodatage', {
            'fields': ('date_creat', 'date_update'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Aperçu BG')
    def apercu_bg(self, obj):
        if obj.bg:
            return format_html(
                '<img src="{}" style="height:48px;border-radius:4px;'
                'object-fit:cover;" />',
                obj.bg.url
            )
        return '—'

    @admin.display(description='Aperçu Poster')
    def apercu_poster(self, obj):
        if obj.poster:
            return format_html(
                '<img src="{}" style="height:48px;border-radius:4px;'
                'object-fit:cover;" />',
                obj.poster.url
            )
        return '—'

    actions = ['activer', 'desactiver']

    @admin.action(description='Activer les slides sélectionnés')
    def activer(self, request, queryset):
        updated = queryset.update(actif=True)
        self.message_user(request, f'{updated} slide(s) activé(s).')

    @admin.action(description='Désactiver les slides sélectionnés')
    def desactiver(self, request, queryset):
        updated = queryset.update(actif=False)
        self.message_user(request, f'{updated} slide(s) désactivé(s).')


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):

    list_display       = ('id', 'apercu_visuel', 'label', 'title',
                          'is_reverse', 'position', 'actif', 'date_update')
    list_display_links = ('id', 'apercu_visuel', 'label')
    list_editable      = ('actif', 'position', 'is_reverse')
    list_filter        = ('actif', 'is_reverse')
    search_fields      = ('label', 'title', 'description')
    ordering           = ('position', 'date_creat')
    readonly_fields    = ('date_creat', 'date_update', 'apercu_visuel')

    fieldsets = (
        ('Contenu', {
            'fields': ('label', 'title', 'description'),
        }),
        ('Visuel', {
            'fields': (('visuel', 'apercu_visuel'),),
        }),
        ('Affichage', {
            'fields': ('is_reverse', 'position', 'actif'),
        }),
        ('Horodatage', {
            'fields': ('date_creat', 'date_update'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Visuel')
    def apercu_visuel(self, obj):
        if obj.visuel:
            return format_html(
                '<img src="{}" style="height:56px;border-radius:6px;'
                'object-fit:cover;" />',
                obj.visuel.url
            )
        return '—'

    actions = ['activer', 'desactiver']

    @admin.action(description='Activer les missions sélectionnées')
    def activer(self, request, queryset):
        updated = queryset.update(actif=True)
        self.message_user(request, f'{updated} mission(s) activée(s).')

    @admin.action(description='Désactiver les missions sélectionnées')
    def desactiver(self, request, queryset):
        updated = queryset.update(actif=False)
        self.message_user(request, f'{updated} mission(s) désactivée(s).')

