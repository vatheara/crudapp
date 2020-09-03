from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")
def hello(request):
    return render(request,'helloworld.html')
def test(request,number):
    text = "<h1>welcome to my app number %s" %number
    return HttpResponse(text)
