from django.contrib import admin
from django.urls import path, include
# from . import views
from .views import login_view

urlpatterns = [
    path('', login_view.index, name='index'),
]