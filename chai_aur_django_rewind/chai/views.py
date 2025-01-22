from django.shortcuts import render,get_object_or_404
from .models import ChaiVarity
from .forms import ChaiVarityForm
from .models import *
# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'all_chai.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chai_detail.html',{'chai':chai})

# Chai Store
def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varities=chai_variety)
    else:
        form = ChaiVarityForm()
    return render(request,'chai_stores.html',{'stores':stores,'form':form})