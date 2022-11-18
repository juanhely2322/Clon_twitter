from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:post_id>/',views.delete_post,name='delete_post'),
    
]