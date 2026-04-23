from django.contrib import admin
from .models import Tag, HeroArticle, NewsArticle, Event


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)
    ordering      = ('name',)


@admin.register(HeroArticle)
class HeroArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'published_at', 'has_video', 'has_link')
    list_filter   = ('published_at',)
    search_fields = ('title', 'description')
    ordering      = ('-published_at',)

    fieldsets = (
        ('Contenu', {
            'fields': ('title', 'description', 'image', 'published_at')
        }),
        ('Liens', {
            'fields': ('link', 'youtube_url')
        }),
    )

    @admin.display(boolean=True, description='Vidéo')
    def has_video(self, obj):
        return bool(obj.youtube_url)

    @admin.display(boolean=True, description='Lien')
    def has_link(self, obj):
        return bool(obj.link)


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display        = ('title', 'author', 'published_at', 'is_published', 'has_image')
    list_filter         = ('is_published', 'published_at', 'tags')
    search_fields       = ('title', 'excerpt', 'author')
    ordering            = ('-published_at',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal   = ('tags',)

    fieldsets = (
        ('Informations', {
            'fields': ('title', 'slug', 'author', 'reading_time', 'tags', 'published_at', 'is_published')
        }),
        ('Image', {
            'fields': ('featured_image', 'image_caption')
        }),
        ('Contenu', {
            'fields': ('excerpt', 'body')
        }),
    )

    @admin.display(boolean=True, description='Image')
    def has_image(self, obj):
        return bool(obj.featured_image)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display        = ('title', 'event_date', 'slug', 'has_image')
    list_filter         = ('event_date',)
    search_fields       = ('title', 'description')
    ordering            = ('event_date',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Informations', {
            'fields': ('title', 'slug', 'event_date')
        }),
        ('Contenu', {
            'fields': ('description', 'image')
        }),
    )

    @admin.display(boolean=True, description='Image')
    def has_image(self, obj):
        return bool(obj.image)