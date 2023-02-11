from django.shortcuts import render, redirect
from .forms.aog_service_form import AogServiceForm
from .forms.aog_item_service_form import AogServiceItemForm
from .forms.dutyperson_form import OndutyServiceForm


from .models.aog_service import AogService
from django.contrib.auth.models import User
from formtools.wizard.views import WizardView, SessionWizardView
# Create your views here.

def service_list(request):
  load_srv = AogService.objects.all()
  users = User.objects.all()
  context = {
        'load_srv': load_srv,
        'users': users,
    }
  return render(request, 'services/services_list.html', context)


def services(request):
  return render(request, 'pages/services/services_list.html', { 'segment': 'services'})

class ServiceWizard(SessionWizardView):
    form_list = [AogServiceForm, AogServiceItemForm, OndutyServiceForm]
    template_name = 'services/add_service.html'

    def done(self, form_list, form_dict, **kwargs):
        first_form = form_dict['0']
        second_form = form_dict['1']
        third_form = form_dict['2']
    

        first = first_form.save()
        second = second_form.save()
        third = third_form.save()
        order = AogServiceForm.save(commit=False)
        order.first = first
        order.second = second
        order.third = third
        order.save()

        return render(self.request, 'services/order_success.html')