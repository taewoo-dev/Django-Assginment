from django.contrib import admin
from django.urls import path

from day1.views import user_list, user_info
from day2.views import todo_list, todo_info

urlpatterns = [
    path('todo/', todo_list, name="todo_list"),
    path('todo/<int:todo_id>/', todo_info, name="todo_info"),
]