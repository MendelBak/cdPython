from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "login_app/index.html")

def register(request):
    errors = User.objects.register_validation(request.POST) # validation being passed from models.py after we pass it our form data and have it validated for us (remember, the postData variable in the models.py file is the form data that we are sending it right here.)
    
    if len(errors) <= 0:
        
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        hashed_password = bcrypt.hashpw((request.POST['password'].encode()), bcrypt.gensalt(5))
        messages.success(request, "You have registered successfully!")
        User.objects.create(first_name = first_name, last_name=last_name, email=email, password=hashed_password) #Passwordhashed with bCrypt
        request.session["first_name"] = first_name #This is for the greeter message.
        return redirect("/success")

    else:
        for x in errors:
            messages.error(request, errors[x])
        return redirect("/")
    
   

def login(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) <= 0:
        messages.success(request, "You have logged in successfully!")
        return redirect("/success")
    else:
        for message in messages:
            message.error(request, errors)
      
        return redirect("/")
        
        

def success(request):
    return render(request, "login_app/success.html")

def logout(request):
    try:
        del request.session["first_name"]
        return redirect("/")
    except KeyError:
        return redirect("/")
