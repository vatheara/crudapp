from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.product_create),
    path('read/',views.product_read),
    path('', views.index, name='index'),
    path('hello',views.index,name='index'),
]
