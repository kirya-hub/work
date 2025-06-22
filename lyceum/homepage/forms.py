from django import forms

class EchoForm(forms.Form):
    text = forms.CharField(
        label="Введите текст",
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        help_text="Этот текст отобразится на следующей странице"
    )