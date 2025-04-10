import django.db.models

import core.models

from catalog.validators import validate_text
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(core.models.PublishedWithNameBaseModel):
    text = django.db.models.TextField(
        validators=[validate_text],
        verbose_name="текст"
    )

    category = django.db.models.ForeignKey(
        "catalog.Category",
        on_delete=django.db.models.CASCADE,
        related_name="items",
        verbose_name="категория"
    )

    tags = django.db.models.ManyToManyField(
        "catalog.Tag",
        related_name="items",
        verbose_name="теги"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name


class Tag(core.models.PublishedWithNameBaseModel):
    slug = django.db.models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="слаг"
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Category(core.models.PublishedWithNameBaseModel):
    slug = django.db.models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="слаг"
    )
    weight = django.db.models.PositiveIntegerField(
        default=100,
        validators=[MinValueValidator(1), MaxValueValidator(32767)],
        verbose_name="вес"
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name
