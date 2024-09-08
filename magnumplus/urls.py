from django.contrib import admin
from django.urls import path
from magnumplus import views

urlpatterns = [
    
    path('gun/',views.gun,name='gun')
]
