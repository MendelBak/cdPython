from django.shortcuts import render, redirect

def index(request):
    response = "Hello, I am your first requesdffdgsdfst!"
    return HttpResponse(response)