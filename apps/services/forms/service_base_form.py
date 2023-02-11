from django import forms
from apps.services.models.aog_service import AogService

class ServiceForm(forms.ModelForm):
    class Meta:
        model = AogService
        fields = ['service_type', 'service_name', 'description' ]
