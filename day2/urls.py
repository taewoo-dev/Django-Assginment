from django.urls import path

from day2.views import todo_list, todo_info, todo_create, todo_update, todo_delete

urlpatterns = [
    path("todo/", todo_list, name="todo_list"),
    path("todo/create/", todo_create, name="todo_create"),
    path("todo/<int:todo_id>/", todo_info, name="todo_info"),
    path("todo/<int:todo_id>/update/", todo_update, name="todo_update"),
    path("todo/<int:todo_id>/delete/", todo_delete, name="todo_delete"),
]
