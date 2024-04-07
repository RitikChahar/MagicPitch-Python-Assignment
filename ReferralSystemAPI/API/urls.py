from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register),
    path('login-user/', views.login),
    path('get-details/', views.details),
    path('get-referrals/', views.refer),
]