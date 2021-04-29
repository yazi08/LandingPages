from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.tea, name = "tea_website" ),
    path('tea_info/',views.tea_info, name ="tea_info" )

]