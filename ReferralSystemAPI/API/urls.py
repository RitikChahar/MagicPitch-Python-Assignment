from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register),
    path('login-user/', views.login),
    path('get-details/<str:user_id>', views.details),
    path('get-referrals/<str:referral_code>', views.refer),
]