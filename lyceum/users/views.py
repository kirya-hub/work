from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.timezone import now
from datetime import timedelta
from .forms import SignUpForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.timezone import now


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Активация по умолчанию
            env_default = settings.DEBUG or settings.DEFAULT_USER_IS_ACTIVE
            user.is_active = env_default
            user.save()

            # отправка письма
            link = request.build_absolute_uri(f"/activate/{user.username}")
            send_mail(
                subject="Активация аккаунта",
                message=f"Привет! Перейди по ссылке для активации: {link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})



def activate_user(request, username):
    user = get_object_or_404(User, username=username)
    if not user.is_active and (now() - user.date_joined) < timedelta(hours=12):
        user.is_active = True
        user.save()
        return HttpResponse("Аккаунт успешно активирован!")
    return HttpResponse("Ссылка недействительна или пользователь уже активирован.")
