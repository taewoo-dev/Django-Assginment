from django.shortcuts import render

from day1.fake_db import user_db


# Create your views here.
def user_list(request):
    user = user_db
    print(user)
    context = {
        "user_list": user
    }
    return render(request, "day1/user_list.html", context)


def user_info(request, user_id):
    user = user_db[user_id]
    context = {
        'user': user
    }
    return render(request, "day1/user_info.html", context)
