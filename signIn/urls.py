
from django.urls import path
from signIn import views

urlpatterns = [
    path('signin/',views.signinview),
]
