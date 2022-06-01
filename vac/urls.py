from django.urls import path
from . import views


app_name = 'vaccine'
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('vaccine/', views.VaccineCreate.as_view(), name='vaccine-create'),
    path('vaccine/detail/', views.VaccineDetail.as_view(), name='vaccine-detail'),

]
