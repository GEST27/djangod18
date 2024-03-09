from django.shortcuts import render
from .models import Product, ProductCategory

def index(request):
    context = {
        'title': 'Магазик'
    }
    return render(request, 'index.html', context = context)

def products(request):
    context = {
        'title':'Магазик-каталог',
        'products' : Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products.html', context = context)

