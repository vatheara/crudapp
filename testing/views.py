from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")
def hello(request):
    return render(request,'index.html')
