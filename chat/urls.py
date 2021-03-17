from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('meal/', meal_info),
]
