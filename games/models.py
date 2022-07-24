from django.db import models
from users.models import User

# Create your models here.

class Game(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "game_user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "game_user2")
    user1_num = models.IntegerField(verbose_name = "유저1 선택숫자")
    user2_num = models.IntegerField(verbose_name = "유저2 선택숫자")
    result = models.CharField(max_length = 63, verbose_name = "게임 결과")
    rule = models.CharField(max_length = 63, verbose_name = "게임 룰")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)




