from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 31, verbose_name = "유저이름")
    score = models.IntegerField(default=0, verbose_name = "총 점수")