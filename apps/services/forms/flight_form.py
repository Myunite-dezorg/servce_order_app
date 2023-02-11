from django import forms
from apps.services.models.aog_service import AogService

class FlightChoiceForm(forms.ModelForm):
    class Meta:
        model = AogService
        fields = ['flight']