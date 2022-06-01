from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import get_user_model

from .forms import RegisterForm

User = get_user_model()


class RegisterView(generic.CreateView):
    model = User
    success_url = reverse_lazy('vaccine:vaccine-create')
    form_class = RegisterForm
    template_name = 'accounts/register_login.html'
