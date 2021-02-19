from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('postform/',views.postformview),
    path('postlist/',views.postlistview),
]
