from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signupview),
    path('thanks/',views.success)
]
