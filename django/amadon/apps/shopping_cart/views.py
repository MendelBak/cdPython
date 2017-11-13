from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "shopping_cart/index.html")

def buy(request):
    print request.POST["buy"]
    return redirect("/")