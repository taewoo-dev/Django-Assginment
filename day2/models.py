from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
User = get_user_model()


class Todo(models.Model):
    title = models.CharField("제목", max_length=50)
    description = models.TextField("해야할 일")
    start_date = models.DateField("해아할 일 시작 날짜")
    end_date = models.DateField("해야할 일 마감 날짜")
    is_completed = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    modified_at = models.DateTimeField("수정 시간", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
