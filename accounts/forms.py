from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
User = settings.AUTH_USER_MODEL

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
    