from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'mail', 'text']
        labels = {
            'name': 'Ваше имя',
            'mail': 'Ваша почта',
            'text': 'Сообщение',
        }
        help_texts = {
            'mail': 'На эту почту мы отправим ответ',
        }
