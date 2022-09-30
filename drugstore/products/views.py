from django.shortcuts import render
from .models import *
# Create your views here.
def products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products/products.html', context)



def product(request, id):
    return render(request, 'products/product.html')


def main(request):
    return render(request, 'main.html')