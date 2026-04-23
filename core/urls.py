from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}
app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('apropos/', views.apropos_page, name="apropos"),
    path('contact/', views.contact_page, name='contact'),
    path('communaute/',views.communaute_page,name='communaute'),
    path('poles/<slug:slug>/', views.pole_detail, name="pole_detail"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)