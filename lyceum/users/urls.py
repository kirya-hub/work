from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, activate_user, user_list, user_detail, profile, CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="main_page"),
        name="logout",
    ),

    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("signup/", signup, name="signup"),
    path("activate/<str:username>", activate_user, name="activate_user"),

    path("", user_list, name="user_list"),
    path("<int:pk>/", user_detail, name="user_detail"),
    path("profile/", profile, name="profile"),
]
