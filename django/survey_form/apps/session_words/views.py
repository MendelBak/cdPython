from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def session_words(request):
    try:
        request.session["words"]
    except KeyError:
        request.session["words"] = []
    # words_list variable is a list that holds a bunch of dictionaries (words_dict). Each dictionary holds each single instance of a submitted new word, the color of the words, and the font size for that word. Iterate through each dictionary in the list in the HTML to print them out while accessing all their pertinent info.
    try:
         request.session["words_list"]
    except KeyError:
        request.session["words_list"] = []
    return render(request, "session_words/index.html")

def add_word(request):
    words_dict = {}
    words_dict["words"] = request.POST["new_word"]
    words_dict["color"] = request.POST["color"]
    # check if big font type is required.
    if "large_font" in request.POST:
        words_dict["font_size"] = "2em"
    else:
        words_dict["font_size"] = "1em"
    #Add the current dictionary to the list.
    request.session["words_list"].append(dict(words_dict))
    print request.session["words_list"]
        
    #timestamp
    request.session["timestamp"] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
   
    
    return redirect("/session_words")

def reset(request):
    del request.session["words"]
    del request.session["words_list"]
    return redirect("/session_words")