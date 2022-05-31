from .models import Vaccine, VaccineShot
from django import forms

class VaccineShotForm(forms.ModelForm):
    class Meta:
        model = VaccineShot
        fields = ['vaccine',]