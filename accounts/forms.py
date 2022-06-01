from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()

class UpdateUser(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','email','phone_number','national_id','birth_date']
    
    # def clean_phone_number(self):
    #     return super().clean_password2()