from django.urls import path
from MyApp import views

urlpatterns = [
    path('home/',views.wish_message),
]