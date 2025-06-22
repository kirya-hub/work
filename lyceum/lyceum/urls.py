from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from catalog.views import main_page


urlpatterns = [
    path("", main_page, name="main_page"),
    path("about/", include("about.urls")),
    path("catalog/", include("catalog.urls")),
    path("admin/", admin.site.urls),
    path('feedback/', include('feedback.urls', namespace='feedback')),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
