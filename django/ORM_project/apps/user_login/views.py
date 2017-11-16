from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
