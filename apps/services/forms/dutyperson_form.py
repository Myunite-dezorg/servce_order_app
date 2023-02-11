from django import forms
from apps.services.models.aog_service import AogService

class OndutyServiceForm(forms.ModelForm):
    class Meta:
        model = AogService
        fields = ['responsibles_persons' ]

