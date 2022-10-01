from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'national_id', 'phone_number', 'birth_date']
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    national_id = models.CharField(
        max_length=14, primary_key=True, unique=True,
        validators=[RegexValidator(r'\d{14}', 'Please enter a valid 14 numbers ID ')]
        )
    phone_number = models.CharField(max_length=11,validators=[
                                    RegexValidator(r'^(01\d{9})$', 'Please enter a valid Phone number')])

    def __str__(self) -> str:
        return self.username
