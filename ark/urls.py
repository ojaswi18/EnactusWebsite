from django.contrib import admin
from django.urls import path,include
from ark import views

urlpatterns = [
    path('homeark',views.home,name="home"),
    path('workark',views.work,name="work"),
    path('patnersark',views.patners,name="patners"), 
    path('moreark',views.more,name="more"), 
]