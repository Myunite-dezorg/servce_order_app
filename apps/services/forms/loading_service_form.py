from django import forms
from apps.services.models.loading_service import LoadingService

class LoadingServiceForm(forms.ModelForm):
    class Meta:
        model = LoadingService
        fields = ['order_type', 'status', 'cancel_reason', 'comment']
        widgets = {
            'status': forms.Select(attrs={'class': 'custom-select'}),
            'cancel_reason': forms.Textarea(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cancel_reason'].required = False
        self.fields['cancel_reason'].widget.attrs['style'] = 'display: none;'

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        cancel_reason = cleaned_data.get('cancel_reason')
        if status == 'canceled' and not cancel_reason:
            self.add_error('cancel_reason', 'Cancel reason is required for canceled orders.')
