from django.contrib import admin
from .models import Contact


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