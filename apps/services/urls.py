from django.urls import path
from .views import ServiceWizard
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('services/list', views.service_list, name='services_list'),
    path('services/add', ServiceWizard.as_view(), name='add_service')
]