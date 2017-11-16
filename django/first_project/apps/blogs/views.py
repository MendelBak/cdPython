from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("Placholder to later display all the list of blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.. OK?")

def create(request):
    return redirect("/blogs")

def show(request, blog_id):
    return HttpResponse("Placeholder to display blog #{}".format(blog_id))

def edit(reqesut, blog_id):
    return HttpResponse("Placeholder to edit blog #{}.".format(blog_id))

def destroy(request, blog_id):
    #this method also contains a blog id that is being sent here from the url.
    return redirect("/blogs")