import django.contrib.admin
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

import catalog.models


class ItemImageInline(django.contrib.admin.TabularInline):
    model = catalog.models.ItemImage
    extra = 1


@django.contrib.admin.register(catalog.models.Item)
class ItemAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        'main_image_preview',
        catalog.models.Item.is_published.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)

    inlines = [ItemImageInline]

    def main_image_preview(self, obj):
        if obj.main_image:
            thumb = get_thumbnail(obj.main_image, '100x100', crop='center', quality=85)
            return format_html('<img src="{}" width="100" height="100">', thumb.url)
        return "—"

    main_image_preview.short_description = "Изображение"


django.contrib.admin.site.register(catalog.models.Category)
django.contrib.admin.site.register(catalog.models.Tag)
