# Generated by Django 5.2b1 on 2025-06-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("mail", models.EmailField(max_length=254, verbose_name="Почта")),
                ("text", models.TextField(verbose_name="Текст обращения")),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "обратная связь",
                "verbose_name_plural": "обратные связи",
            },
        ),
    ]
