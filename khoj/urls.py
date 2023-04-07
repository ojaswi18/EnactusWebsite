from django.contrib import admin
from django.urls import path,include
from khoj import views

urlpatterns = [
    path('homekhoj',views.home,name="home"),
    path('workkhoj',views.work,name="work"),
    path('patnerskhoj',views.patners,name="patners"), 
    path('morekhoj',views.more,name="more"), 
]