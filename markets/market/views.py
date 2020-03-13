from django.shortcuts import render,redirect
from .models import *



def index(request):
    salelists = SaleList.objects.all()
    return render(request,'index.html',locals())


def login(request):
    return render(request,'login.html',locals())


def add_product(request):
    if request.method == 'POST':
        code = request.POST.get('productNo')
        SaleList.objects.create(productno=code)
    return redirect('index')


def delete_product(request,productid):
    SaleList.objects.filter(id=productid).delete()
    return redirect('index')

# Create your views here.
