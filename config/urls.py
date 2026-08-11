from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    # Ensure homepage is reachable at root (avoid missing root when using i18n_patterns)
    path('', include('classic.urls')),
]

urlpatterns += i18n_patterns(
    path('Administrateur/', include('gestion_vehicules.urls')),
    path('auth/', include('auth_Admin.urls')),
    path('', include('classic.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)