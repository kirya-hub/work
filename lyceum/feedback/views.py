from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    form = FeedbackForm(request.POST or None)
    success = False

    if request.method == 'POST' and form.is_valid():
        feedback_obj = form.save()

        # Отправляем письмо
        send_mail(
            subject='Обратная связь от пользователя',
            message=feedback_obj.text,
            from_email=settings.DJANGO_MAIL,
            recipient_list=[feedback_obj.mail],
            fail_silently=False,
        )

        success = True
        return redirect(f"{request.path}?success=true")

    # Отображение страницы с формой
    return render(request, 'feedback/feedback.html', {
        'form': form,
        'success': request.GET.get('success') == 'true'
    })
