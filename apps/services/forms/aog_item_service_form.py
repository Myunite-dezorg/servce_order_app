from django import forms
from apps.services.models.aog_service import AogService

class AogServiceItemForm(forms.ModelForm):
    class Meta:
        model = AogService
        fields = ['aog_item' ]

