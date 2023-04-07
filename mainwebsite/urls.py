from django.contrib import admin
from django.urls import path,include
from mainwebsite import views

urlpatterns = [
    path('',views.home,name="home"),
    path('projects',views.projects,name="projects"),
    path('achievements',views.achievements,name="achievements"),
    path('achievementsdetail/<str:slug>',views.achievementsdetail,name="achievementsdetail"),
    path('about',views.about,name="about"),
    path('team',views.team,name="team"),
    path('contact',views.contact,name="contact")
]
