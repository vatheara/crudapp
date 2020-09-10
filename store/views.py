from django.shortcuts import render, redirect
from store.forms import ProductForm
from store.models import Product
from django.http import HttpResponse

def create(request):
    product1 = Product(
        p_id = "1",
        p_name = "coca",
        p_qty = "12",
        p_price = "1.2"
    )
    product1.save()
    return HttpResponse("<b> created 1 product! </b>")
def read(request):
    products = Product.objects.all()
    res = 'print all products in the database <br>'
    for i in products:
        res += "Product ID:" + i.p_id + "<br>Product Name:" + i.p_name + "<br>Product QTY:" + i.p_qty + "<br>Product Price:" + i.p_price
    return HttpResponse(res)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

