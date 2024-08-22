from django.shortcuts import render

from day2.models import Todo


# Create your views here.

def todo_list(request):
    todo_list = Todo.objects.all()
    context = {
        "todo_list": todo_list
    }
    return render(request,'day2/todo_list.html', context)


def todo_info(request, todo_id):
    todo_info = Todo.objects.get(id=todo_id)
    context = {
        "todo_info": todo_info,
    }
    return render(request, 'day2/todo_info.html', context)