from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

app_name = "games"

urlpatterns = [
    path('', views.main, name="main"),
    path('play', views.play, name="play"),
    path('reattack', views.reattack, name="reattack"),
    path('accounts/',include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name = 'main.html'), name = 'main'),
    path('accounts/', include("allauth.urls")),
]