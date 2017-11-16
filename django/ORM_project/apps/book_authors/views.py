from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Hello, I am your firsrdgsgfdgfsdfgsdt request!"
    return HttpResponse(response)