from django.db import models


# Validation begins here, by creating a user.Manager
# first_name must be over 2 chars
# first_name must be chars not ints
# last_name must be over 2 chars
# last_name must be chars not ints
class UserManager(models.Manager):
    def user_validation(self, postData):
        
        errors = {}

        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First Name must be over 2 characters"

        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last Name must be over 2 characters"

        if len(postData["email"]) < 2:
            errors["email"] = "Email must be over 2 characters"
        
        return errors


# Validation must occur before the class since the data needs to be validated before it is entered into the DB.
# class User_Manager(models.manager):
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()





    