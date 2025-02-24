from django.shortcuts import render, get_object_or_404, redirect
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

def edit_product(request, product_id):
    Product = get_object_or_404(product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=Product) # request.POST = Text File, 
        if form.is_valid():
            form.save()
            return redirect('clothing')
    else:
        form = ProductForm(instance=Product)
    
    return render(request, 'clothing/edit_product.html',{'form':form})

def delete_product(request, product_id):
    Product = get_object_or_404(product, id=product_id)

    if request.method == "POST":
        Product.delete() 
        return redirect('clothing')
    
    return render(request, 'clothing/confirm_delete.html',{'product':product})

    