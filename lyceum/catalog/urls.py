import django.urls

import catalog.views


urlpatterns = [
    django.urls.path("", catalog.views.item_list),
    django.urls.path("<int:pk>/", catalog.views.item_detail),
    #django.urls.path('item/<int:item_id>/', catalog.views.item_detail, name='item_detail'),
]
