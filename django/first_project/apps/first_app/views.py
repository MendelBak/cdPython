from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mendel"
    }
    return render(request, "first_app/index.html", context)

def new(request):
    response = "This is also placeholder text to display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def show(request, blog_id):
    response = "Placeholder text to display blog {}".format(blog_id)
    return HttpResponse(response)

def edit(request, blog_id):
    return HttpResponse("Placeholder to edit blog {}".format(blog_id))

def destroy(request, blog_id):
    return redirect("/")
