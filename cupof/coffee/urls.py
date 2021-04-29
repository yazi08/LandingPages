from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.coffee, name = "coffee_website" ),
    path('coffee_info/',views.coffee_info, name ="coffee_info" )

]

