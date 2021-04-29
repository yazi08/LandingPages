from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.members, name = "members" ),
    path('members_info/',views.members_info, name ="members_info" )


]