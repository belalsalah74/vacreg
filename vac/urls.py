from django.urls import path
from . import views


app_name = 'vac'
urlpatterns = [
    path('',views.Index.as_view(),name='home'),
    path('vaccine/',views.VaccineRegister.as_view(),name='vaccine'),
]

