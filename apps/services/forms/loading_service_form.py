from django import forms
from apps.services.models.loading_service import LoadingService

class LoadingServiceForm(forms.ModelForm):
    class Meta:
        model = LoadingService
        fields = ['loading_address', 'loading_date', 'loading_time', 'loading_contact_person', 'loading_contact_phone']
        
    loading_date = forms.DateField(widget=forms.SelectDateWidget)
    loading_time = forms.TimeField(widget=forms.TimeInput)