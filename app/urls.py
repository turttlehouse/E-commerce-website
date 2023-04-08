
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',views.home),
    path('aboutproduct/<int:id>',views.aboutproduct),
    path('home/mensproduct',views.mensproduct),
    path('home/womenproduct',views.womenproduct),
    path('home/upload',views.Createuser),
    path('',views.loginuser,name='login'),
    path('signupclients/',views.signupclients),
    path('logoutclients/',views.logoutclients),
    path('search/',views.searchproduct,name="searchbox"),
    
]