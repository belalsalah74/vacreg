from django.shortcuts import render
from django.views import generic

from django.contrib.auth import get_user_model

from .forms import RegisterForm

User = get_user_model()

class RegisterView(generic.CreateView):
    model = User
    success_url = '/'
    form_class = RegisterForm

