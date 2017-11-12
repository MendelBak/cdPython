from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "form/index.html")

def process_form(request):
    try:
        request.session["counter"]
    except KeyError:
        request.session["counter"] = 0
    request.session["counter"] += 1
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["fav_language"] = request.POST["fav_language"]
    request.session["comments"] = request.POST["comments"]
    print request.POST["location"]
    print request.session["counter"]
    return redirect("/result")

def result(request):
    return render(request, "form/result.html")

def go_back(request):
    return redirect("/")

def clear_counter(request):
    del request.session["counter"]
    return redirect("/")