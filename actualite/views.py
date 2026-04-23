from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, HeroArticle, Event


def news_index(request):
    hero    = HeroArticle.objects.order_by('-published_at').first()
    news    = NewsArticle.objects.filter(is_published=True).order_by('-published_at')[:10]
    events  = Event.objects.all().order_by('event_date')

    return render(request, 'actualite/actualites_page.html', {
        'hero':   hero,
        'news':   news,
        'events': events,
    })

def news_detail(request, slug):
    """
    Vue de détail d'un article de news.
    - article      : l'article demandé (publié uniquement)
    - recent_articles : 3 derniers articles (sidebar), hors article courant
    - related_articles: jusqu'à 3 articles liés (par tag commun), sinon les 3 derniers
    """
    article = get_object_or_404(
        NewsArticle,
        slug=slug,
        is_published=True,
    )

    recent_articles = (
        NewsArticle.objects
        .filter(is_published=True)
        .exclude(pk=article.pk)
        .order_by('-published_at')[:3]
    )
    
    article_tags = article.tags.all()

    if article_tags.exists():
        related_articles = (
            NewsArticle.objects
            .filter(is_published=True, tags__in=article_tags)
            .exclude(pk=article.pk)
            .distinct()
            .order_by('-published_at')[:3]
        )
    else:
        related_articles = (
            NewsArticle.objects
            .filter(is_published=True)
            .exclude(pk=article.pk)
            .order_by('-published_at')[:3]
        )

    context = {
        'article': article,
        'recent_articles': recent_articles,
        'related_articles': related_articles,
    }

    return render(request, 'actualite/news_detail.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'actualite/event_detail.html', {'event': event})