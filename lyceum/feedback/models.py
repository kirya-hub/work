from django.db import models

class Feedback(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )

    mail = models.EmailField(
        verbose_name="Почта"
    )

    text = models.TextField(
        verbose_name="Текст обращения"
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )

    class Meta:
        verbose_name = "обратная связь"
        verbose_name_plural = "обратные связи"

