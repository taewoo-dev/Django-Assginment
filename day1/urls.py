from django.contrib import admin
from django.urls import path

from day1.views import user_list, user_info

urlpatterns = [
    path('users/', user_list, name="users"),
    path('users/<int:user_id>/', user_info, name="user_info"),
]