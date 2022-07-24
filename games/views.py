
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Game,User
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.

@csrf_exempt
def main(request):

    games = Game.objects.all()

    context = {
        "games":games
    }
    return render(request, template_name='games/main.html', context=context)

@login_required
def play(request):
    if request.method == "POST":
        user2_id = User.objects.get(id = request.POST["user2"])
        user1_num = request.POST["user1_num"]
        user1 = User.objects.get(id=1)
        rule = random.choice(["big","small"])

        Game.objects.create(
        user2=user2_id,
        user2_num=0,
        user1_num=user1_num,
        user1 = user1,
        rule = rule,
        result = "ing"
        )
        return redirect("/")

    users = User.objects.all()
    cards = [1,2,3,4,5,6,7,8,9,10]
    r_cards = random.sample(cards,5)
    context = {"users": users,"r_cards":r_cards}
    return render(request, template_name='games/play.html', context=context)

@login_required
def reattack(request):
    cards = [1,2,3,4,5,6,7,8,9,10]
    r_cards = random.sample(cards,5)
    context = {"r_cards":r_cards}
    return render(request, template_name='games/reattack.html', context=context)