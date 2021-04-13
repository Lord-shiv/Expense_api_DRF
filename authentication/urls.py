from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email_verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refer"),
    path('request-reset/', RequestPasswordResetEmail.as_view(), name="reset_email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name="password_reset"),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name="password_reset_complete"),
]