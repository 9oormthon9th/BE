from django.urls import path
from .kakaoapi import views

urlpatterns = [
    path('',views.index),
]