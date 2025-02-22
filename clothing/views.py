from django.shortcuts import render, HttpResponse
from clothing.models import product
from .forms import ProductForm

# Create your views here.
def clothing(request):
    form = ProductForm()
    pro_img = product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
    return render(request, "clothing/fashion.html", {"pro_img":pro_img, "form":form})

    