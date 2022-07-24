from django.shortcuts import render

from .models import User
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
# Create your views here.

def all_user(requests):
    
    if requests.method == "GET":
        users = User.objects.all()
        
        return JsonResponse(users = users)
