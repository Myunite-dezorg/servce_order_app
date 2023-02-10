from django import forms
from apps.services.models.abstract_class import AbstractService


class ServiceServiceForm(forms.ModelForm):
    class Meta:
        model = AbstractService
        fields = [ 
                  'order_type', 
                  'status', 
                  'payment_status', 
                  'cancel_reason', 
                  ]
        
    order_type = forms.ChoiceField(choices=AbstractService.ORDER_TYPE_CHOICES, widget=forms.RadioSelect)
    status = forms.ChoiceField(choices=AbstractService.ORDER_STATUS_CHOICES)
    comment = forms.CharField(required=False)