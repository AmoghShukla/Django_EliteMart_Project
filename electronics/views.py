from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    prod = Product.objects.all()
    return render(request, "electronics/home.html", {"prod":prod})

def electronics(request):
    return render(request, "electronics/home.html")  

# Clothing page
def clothing(request):
    return render(request, "clothing/fashion.html")  

# Grocery page
def grocery(request):
    return render(request, "grocery/groceries.html") 
