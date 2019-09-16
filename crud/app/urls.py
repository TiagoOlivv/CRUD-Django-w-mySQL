from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', createTask, name='createTask'),
    path('update/<int:id>', updateTask, name='updateTask'),
    path('remove/<int:id>', removeTask, name='removeTask')
]