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
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


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
    return render(request, "registration/signup.html", {"form": form})


def activate_user(request, username):
    user = get_object_or_404(User, username=username)
    if not user.is_active and (now() - user.date_joined) < timedelta(hours=12):
        user.is_active = True
        user.save()
        return HttpResponse("Аккаунт успешно активирован!")
    return HttpResponse("Ссылка недействительна или пользователь уже активирован.")


def user_list(request):
    users = User.objects.filter(is_active=True).select_related("profile")
    return render(request, "users/user_list.html", {"users": users})


def user_detail(request, pk):
    user_obj = get_object_or_404(User, pk=pk)
    return render(request, "users/user_detail.html", {"user_obj": user_obj})


@login_required
def profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)
    return render(request, "users/profile.html", {"form": form})
