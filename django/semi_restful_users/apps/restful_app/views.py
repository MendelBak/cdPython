from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

def index(request):
    dbData = {
        "user_data_key" : User.objects.all()
    }
    return render(request, "restful_app/index.html", dbData)


def new_user(request):
    return render(request, "restful_app/create.html")
    

def create(request):    
    new_first_name = request.POST['first_name']
    new_last_name = request.POST["last_name"]
    new_email = request.POST["email"]

    # Need to have validation before adding into database but after they are assigned variables.
    errors = User.objects.user_validation(request.POST) #  This is passing the form data to the validation function in the models.py file, running the validation on the data, and returning it saved into our new variable called "errors"
    if len(errors) <= 0:
        new_first_name = request.POST["first_name"]
        new_last_name = request.POST["last_name"]
        new_email = request.POST["email"]
        messages.success(request, "A new user has been added.")
        User.objects.create(first_name=new_first_name, last_name=new_last_name, email=new_email)
        dbData = User.objects.last()
        return redirect("/show/{}".format(dbData.id), dbData)
    else:
        for x in errors:
            messages.error(request, errors[x])
    return redirect("/new_user")
    


def show(request, user_id): #Need to have the user_id paramater in order to pass the variable into the view from the urls.py page
    dbData = {
        "user_data_key" : User.objects.get(id=user_id),
    }
    return render(request, "restful_app/show.html", dbData) #Don't forget to pass the dictionary through to the html doc.


def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/")


def edit(request, user_id):
    dbData = {
        "user_data_key" : User.objects.get(id=user_id),
    }
    return render(request, "restful_app/edit.html", dbData)


def update_user(request, user_id):
    dbData = {
        "user_data_key" : User.objects.get(id=user_id),
    }

    update_record = User.objects.get(id=user_id)

    update_record.first_name = request.POST["first_name"]
    update_record.save()
    update_record.last_name = request.POST["last_name"]
    update_record.save()
    update_record.email_name = request.POST["email"]
    update_record.save()
    # You can pass in variables to your url by using string formatting.
    return redirect("/show/{}".format(user_id), dbData) #redirect to show the newly updated user.