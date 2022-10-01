from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UpdateUser(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': self.fields[field].label})
            self.fields[field].help_text = None
            self.fields[field].label = ""


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2', 'email', 'phone_number', 'national_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': self.fields[field].label})
            self.fields[field].help_text = None
            self.fields[field].label = ""
