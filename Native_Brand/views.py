from django.shortcuts import render
from products.models import product,logo

def home(request):
    item=product.objects.all()
    return render(request,'base.html',{'items':item})


def logo(request):
    Hlogo = logo.objects
    return render(request, 'base.html',{'logos':Hlogo})