from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create),
    path('read/',views.read),
    path('delete/<int:id>',views.Delete),
    path('', views.index, name='index'),
    path('hello/',views.index,name='index'),
]
