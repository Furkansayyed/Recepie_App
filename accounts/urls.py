from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

urlpatterns = [
    path('register', views.registerUsers, name="RegisterUsers"),
    path('login', views.loginUsers, name="loginUsers"),
    path('logout', views.logoutUsers, name="logoutUsers")
]
