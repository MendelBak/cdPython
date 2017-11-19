from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



# Validation
# Check to ensure both passwords entered on registration match.
class UserManager(models.Manager):
    def register_validation(self, postData): # postData is the form data that is passed through by whatever view calls this function. 
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First Name must be over 2 characters"

        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last Name must be over 2 characters"

        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Email is incorrect"

        if postData["password"] != postData["password2"]:
            errors["password"] = "Passwords don't match"
        
        return errors

    def login_validation(self, postData):
        errors = {}

        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Email was entered incorrectly"
        try:
            check_email = self.filter(email=postData['email'])
        except Exception:
            print "These are the exceptions", Exception
        check_pw = self.filter(password=postData["password"]) #.self.User.objects?
        print check_pw
        if not bcrypt.checkpw(postData['password'].encode(), postData.password.encode()):
            errors["password"] = "Password is incorrect"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
