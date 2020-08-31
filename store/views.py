from django.shortcuts import render, redirect
from product.forms import ProductForm
from product.models import Product
from django.http import HttpResponse

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/read')
            except:
                pass
    else:
        form = ProductForm()
    return render(request,'create.html',{'form':form})

def product_read(request):
    products = Product.objects.all()
    return render(request,'read.html',{'products':products})
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

