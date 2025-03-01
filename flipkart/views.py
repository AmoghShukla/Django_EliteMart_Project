from django.shortcuts import render

def home(request):
    return render(request, "flipkart/home.html")

def grocery(request):
    return render(request, "grocery/groceries.html")

def electronics(request):
    return render(request, "electronics/home.html")

def clothing(request):
    return render(request, "clothing/fashion.html")
