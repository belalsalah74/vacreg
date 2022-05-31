from django.shortcuts import render
from django.views import generic
from vac.forms import VaccineShotForm
from vac.models import VaccineShot

class Index(generic.TemplateView):
    template_name = 'vac/index.html'


class VaccineRegister(generic.CreateView):
    model = VaccineShot
    form_class = VaccineShotForm