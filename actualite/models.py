from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import re


# =========================
# TAG
# =========================
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Tag"
        verbose_name_plural = "Tags"
        ordering            = ('name',)


# =========================
# HERO
# =========================
class HeroArticle(models.Model):
    title        = models.CharField(max_length=255)
    description  = models.TextField()
    image        = models.ImageField(upload_to='hero/', blank=True, null=True)
    published_at = models.DateField(default=timezone.now)
    link         = models.URLField(blank=True, null=True)
    youtube_url  = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_youtube_embed_url(self):
        if not self.youtube_url:
            return None
        match = re.search(r'(?:v=|youtu\.be/|shorts/)([a-zA-Z0-9_-]{11})', self.youtube_url)
        if match:
            return f'https://www.youtube.com/embed/{match.group(1)}'
        return None

    class Meta:
        verbose_name        = "Article à la une"
        verbose_name_plural = "Articles à la une"
        ordering            = ('-published_at',)


# =========================
# ARTICLE
# =========================
class NewsArticle(models.Model):
    title          = models.CharField(max_length=255)
    slug           = models.SlugField(max_length=255, unique=True, blank=True)
    excerpt        = models.TextField()
    author         = models.CharField(max_length=100, default='Admin')
    reading_time   = models.PositiveIntegerField(default=5)
    tags           = models.ManyToManyField(Tag, blank=True)
    featured_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    image_caption  = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True, null=True)
    published_at   = models.DateField(default=timezone.now)
    is_published   = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "Article"
        verbose_name_plural = "Articles"
        ordering            = ('-published_at',)


# =========================
# EVENT
# =========================
class Event(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to='events/', blank=True, null=True)
    event_date  = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "Événement"
        verbose_name_plural = "Événements"
        ordering            = ('event_date',)