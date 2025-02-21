from django.shortcuts import render, HttpResponse
from .models import DRESS

# Create your views here.
def clothing(request):
    pro_img = DRESS.objects.all()
    return render(request, "clothing/fashion.html", {"pro_img":pro_img})
    