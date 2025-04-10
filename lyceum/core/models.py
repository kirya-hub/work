import django.db.models


class PublishedWithNameBaseModel(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=150,
        unique=True,
        verbose_name="название"
    )
    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="опубликовано"
    )

    class Meta:
        abstract = True
