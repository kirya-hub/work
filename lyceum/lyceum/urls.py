from django.conf import settings
import django.contrib.admin
import django.urls

import about.urls
import catalog.urls
import homepage.urls

from django.urls import include, path


urlpatterns = [
    django.urls.path("", django.urls.include(homepage.urls)),
    django.urls.path("about/", django.urls.include(about.urls)),
    django.urls.path("catalog/", django.urls.include(catalog.urls)),
    django.urls.path("admin/", django.contrib.admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
