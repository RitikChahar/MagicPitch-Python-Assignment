from django import forms
from .models import User, Referral

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'referral_code']

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referred_by', 'referred_user','referral_points']