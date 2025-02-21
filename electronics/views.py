from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    prod = Product.objects.all()
    return render(request, "electronics/home.html", {"prod":prod})
    