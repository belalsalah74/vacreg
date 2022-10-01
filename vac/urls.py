from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'vaccine'
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('vaccine/', views.VaccineCreate.as_view(), name='vaccine-create'),
    path('vaccine/detail/', views.VaccineDetail.as_view(),name='vaccine-detail'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
