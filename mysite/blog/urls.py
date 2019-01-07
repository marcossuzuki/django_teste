from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
]