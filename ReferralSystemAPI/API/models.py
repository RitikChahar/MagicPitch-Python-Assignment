from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Referral(models.Model):
    referred_by = models.CharField(max_length=100)
    referred_user = models.CharField(max_length=100)
    referral_points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)