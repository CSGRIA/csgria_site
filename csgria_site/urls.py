from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('secure-panel-csgria/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('actualites/', include(('actualite.urls', 'actualite'), namespace='actualite')),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)