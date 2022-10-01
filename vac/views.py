from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VaccineShot
from .forms import VaccineShotForm


class Index(generic.TemplateView):
    template_name = 'vac/index.html'


class VaccineDetail(LoginRequiredMixin, generic.DetailView):

    def get(self, request):
        user = request.user
        try:
            shot = VaccineShot.objects.get(user__pk=user.pk)
        except VaccineShot.DoesNotExist:
            messages.error(request, "You haven't registered for a shot yet.")
            return redirect('vaccine:vaccine-create')

        return render(request, 'vac/vaccineshot_detail.html', {'object': shot, 'now': timezone.now().date()})


class VaccineCreate(LoginRequiredMixin, generic.CreateView):
    model = VaccineShot
    form_class = VaccineShotForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

