from django.shortcuts import render
from .forms.abstract_service_form import AbstractOrder

# Create your views here.
def add_service_loadin(request):
    if request.method == 'POST':
        form = AbstractOrderForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            if order_type == 'loading':
                form = LoadingOrderForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('order_list')
            elif order_type == 'offloading':
                form = OffloadingOrderForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('order_list')
    else:
        form = AbstractOrderForm()
    return render(request, 'add_order.html', {'form': form})