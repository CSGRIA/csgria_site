from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name='core'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('apropos/',views.apropos_page,name="apropos"),
    path('communaute/',views.communaute_page,name='communaute'),
    path('contact/',views.contact_page,name='contact')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)