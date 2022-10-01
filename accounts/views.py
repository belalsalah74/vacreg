from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib.auth import login,authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

from .forms import RegisterForm

User = get_user_model()

class RegisterView(generic.CreateView):
    model = User
    success_url = reverse_lazy('vaccine:vaccine-create')
    form_class = RegisterForm
    template_name = 'accounts/register_login.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('vaccine:vaccine-create')
