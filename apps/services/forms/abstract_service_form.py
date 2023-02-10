from django import forms
from apps.services.models.abstract_class import AbstractService


class ServiceServiceForm(forms.ModelForm):
    class Meta:
        model = AbstractService
        fields = ['order_number', 
                  'order_type', 
                  'status', 
                  'payment_status', 
                  'cancel_reason', 
                  'date_created',
                  'date_updated',
                  'created_by',
                  'modified_by',
                  ]
        
    order_type = forms.ChoiceField(choices=AbstractService.ORDER_TYPE_CHOICES, widget=forms.RadioSelect)
    status = forms.ChoiceField(choices=AbstractService.STATUS_CHOICES)
    comment = forms.CharField(required=False)