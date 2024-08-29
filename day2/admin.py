from django.contrib import admin

from day2.models import Todo, Comment


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    pass
