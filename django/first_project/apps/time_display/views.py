from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    request.session["clock"] = {
        "time": strftime("%b %d, %Y, %I %p - %Z", gmtime())
    }
    return render(request, "time_display/index.html")