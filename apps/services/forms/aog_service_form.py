from django import forms
from apps.services.models.aog_service import AogService

class AogServiceForm(forms.ModelForm):
    class Meta:
        model = AogService
        fields = ['service_name', 'description', ]

