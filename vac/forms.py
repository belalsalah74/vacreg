from .models import Vaccine, VaccineShot
from django import forms


class VaccineShotForm(forms.ModelForm):
    class Meta:
        model = VaccineShot
        fields = ['vaccine', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vaccine'].widget.attrs.update({'class': 'form-select mb-3','label':''})
        self.fields['vaccine'].label=''
        self.fields['city'].widget.attrs.update({'class': 'form-select mb-3'})
        
