from django.contrib import admin
from django.urls import path
from magnumplay import views

urlpatterns = [

    path('',views.fun,name='fun'),
    path('index',views.yup,name='yup')
]
