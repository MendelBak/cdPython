from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    try:
        request.session["counter"]
    except:
        request.session["counter"] = 0
    return render(request, "random_word/index.html")

def generate(request):
    request.session["counter"] += 1
    request.session["random_word"] = {
        "word" : get_random_string(length=14)
        }
    return redirect("/")

def reset(request):
    request.session["counter"] = 0
    request.session["random_word"] = ""
    return redirect("/")