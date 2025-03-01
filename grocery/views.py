from django.shortcuts import render
from .models import Product

# Create your views here.
def grocery(request):
    prod = Product.objects.all()
    return render(request, "grocery/groceries.html", {"prod":prod})


def electronics(request):
    return render(request, 'electronics/home.html')

def home_flipkart(request):
    return render(request, 'flipkart/home.html')

def clothing(request):
    return render(request, 'clothing/fashion.html')