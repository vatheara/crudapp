from django.urls import path
from . import views
urlpatterns = [
    path('',views.test),
    path('fb_cmt/',views.fb_cmt),
]
