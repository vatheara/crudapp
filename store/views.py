from django.shortcuts import render, redirect
from store.forms import ProductForm
from store.models import Product
from django.http import HttpResponse

def create(request):
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
def read(request):
    products = Product.objects.all()
    return render(request,'list.html',{'p':products,})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

