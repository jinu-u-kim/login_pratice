# admin.py
from django.contrib import admin
from .models import Game,User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


