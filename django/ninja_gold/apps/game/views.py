from django.shortcuts import render, HttpResponse, redirect
from random import randint
from datetime import datetime

def index(request):
    try:
         request.session["total_gold"]
    except:
        request.session["total_gold"] = 0
    if not "log_message" in request.session:
        request.session["log_message"] = []
    return render(request, "game/index.html")

def process_money(request, location):
    #this is to print the proper message to the log telling the player whether he "won" or "lost" gold.
    verb = "won"
    if location == "farm":
        new_gold = randint(10, 20)
    elif location == "cave":
       new_gold = randint(5, 10)
    elif location == "house":
       new_gold = randint(2, 5)
    elif location == "casino":
       new_gold = randint(-50, 50)
       #this is to print the proper message to the log telling the player whether he "won" or "lost" gold.
       if new_gold < 0:
           verb = "lost"
    timestamp = datetime.now().strftime("%Y/%m/%d %I:%M%p")
    temp_log = "You've {} {} gold! ({})".format(verb, new_gold, timestamp)
    
    if "log_message" in request.session:
        request.session["log_message"].append(temp_log)
    else:
        request.session["log_message"] = [temp_log]
    request.session["total_gold"] += new_gold

    return redirect("/")

def reset(request):
    del request.session["total_gold"]
    del request.session["log_message"]
    return redirect("/")