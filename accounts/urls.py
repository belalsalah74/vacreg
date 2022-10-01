from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/register_login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/register_login.html'), name='logout'),
]
