from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import about.urls
import catalog.urls
import homepage.urls


urlpatterns = [
    path("", include(homepage.urls)),
    path("about/", include(about.urls)),
    path("catalog/", include(catalog.urls)),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
