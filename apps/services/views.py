from django.shortcuts import render, redirect
from .forms.abstract_service_form import ServiceServiceForm
from .forms.loading_service_form import LoadingServiceForm
from .models.loading_service import LoadingService
from django.contrib.auth.models import User
# Create your views here.

def service_list(request):
  load_srv = LoadingService.objects.all()
  users = User.objects.all()
  context = {
        'load_srv': load_srv,
        'users': users,
    }
  return render(request, 'services/services_list.html', context)


def services(request):
  return render(request, 'pages/services/services_list.html', { 'segment': 'services'})

def add_service_loadin(request):
    if request.method == 'POST':
        form = ServiceServiceForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            if order_type == 'loading':
                form = LoadingServiceForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('order_list')
            elif order_type == 'offloading':
                form = OffloadingOrderForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('order_list')
    else:
        form = ServiceServiceForm()
    return render(request, 'add_order.html', {'form': form})