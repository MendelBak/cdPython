from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
    return HttpResponse("Placeholder to display all the surveys created")