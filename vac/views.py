from django.shortcuts import redirect, render
from django.views import generic
from vac.forms import VaccineShotForm
from vac.models import VaccineShot
from django.utils import timezone

class Index(generic.TemplateView):
    template_name = 'vac/index.html'


class VaccineDetail(generic.DetailView):
    model = VaccineShot
    form_class = VaccineShotForm
    extra_context = {'now': timezone.now().date()}



class VaccineCreate(generic.CreateView):
    model = VaccineShot
    form_class = VaccineShotForm



    def post(self, request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            shot = form.save(commit=False)
            shot.user = request.user
            shot.save()
            return redirect('vac:home')

        return super().get(request,*args, **kwargs)