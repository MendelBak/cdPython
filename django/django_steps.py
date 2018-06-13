


#(This boilerplate works with Python 3.7 and Django 2.0)
# (First working project using this template is the ajaxPagination project in my cdPython repo)
# SETUP
# 1) Ensure that python, pip, virtualenv, and django are installed
    --> pip install virtualenv
# 2) create a django virtual environment (using bash or MacOS)
    --> virtualenv djangoEnjv
    --> source djangoEnv/Scripts/activate
        #2) (If you're using Windows or cmd or Powershell)
        --> python -m virtualenv djangoEnv
        --> call djangoEnv/Scripts/activate
# 3) Install django inside your virtual environment
    -- > pip install django



# CREATION
# 1) create a Django project
    --> django-admin startproject <project name goes here>

# 2) create an 'apps' folder
    --> cd <project name goes here>
    --> mkdir apps

# 3) create dunder-file in apps folder
    --> cd apps
    --> touch __init__.py

# 4) create an app in the 'apps' folder
    --> python ../manage.py startapp <app name goes here>

#5) create urls.py file inside of newly created app
    --> cd <app name goes here>
    --> touch urls.py

# 6) Run migrations
    --> cd ../../
    --> python manage.py migrate

# 7) Run the project (while in the root directory)
    --> python manage.py runserver

#EDIT
#1) settings.py in project folder -> register newly created app
    in INSTALLED_APPS add
    'apps.<appname>'

#2) include app urls.py in >>project's<< urls.py and delete the two other "from" statements.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.testApp.urls')),
    path('admin/', admin.site.urls),
]

# 3) Add route to the >>app's<< urls.py file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# 4) Create a method in the app's views.py
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# 5) Go back to main project folder
    --> python manage.py runserver
    --> python manage.py makemigrations
    --> python manage.py migrate

# 6) If you're having a persistent error where you cannot import packages create a .pylintrc file in the root directory and place this inside it.
[MASTER]
init-hook='import sys; sys.path.append("C:\Users\mende\AppData\Roaming\Python\Python37\Lib\site-packages")'




# Creating models
  make ERD diagram
  python manage.py graph_models -a -o myapp_models.png

Get table name raw queries
    User._meta.db_table


apps/appname/templates/

# Models setup example
from __future__ import unicode_literals
from django.db import models

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas") #Foreign key connecting this to the dojo table, since many ninjas are in one dojo, but not vice vesa (Foreign Keys are always a One To Many Relationship).1459
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# ORM COMMANDS

# opens files from models.py (DO INSIDE SHELL)
from apps.<appname>.models import *

# Importing data to the shell
from apps.<appname>.models import <modelname>

# Creating a new record
Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc) # creates a new record in the Blog table
Blog.objects.create(name="Star Wars Blog", desc="Everything about Star Wars") # creates a new blog record
Blog.objects.create(name="CodingDojo Blog") # creates a new blog record with the empty desc field
Alternative way of creating a record
b = Blog(name="Disney Blog", desc="Disney stuff")
b.name = "Disney Blog!"
b.desc = "Disney stuff!!!"
b.save()

# Basic Retrieval
Blog.objects.first() - retrieves the first record in the Blog table
Blog.objects.last() - retrieves the last record in the Blog table
Blog.objects.all() - retrieves all records in the Blog table
Blog.objects.count() - shows how many records are in the Blog table

# Updating the record - once you obtain an object that has the record you want to modify, use save() to update the record.  For example
b = Blog.objects.first() # gets the first record in the blogs table
b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
b.save() # updates the blog record

# Deleting the record - use delete().  For example
b = Blog.objects.get(id=1)
b.delete() # deletes that particular record
# OR
Blog.objects.get(id=1).delete()
# OR
Blog.objects.all().delete()


# Other methods to retrieve records
Blog.objects.get(id=1) - retrieves where id is 1; get only retrieves 1 record
Blog.object.filter(name="mike") - retrieves records where name is "mike"; returns multiple records
Blog.objects.exclude(name="mike") - opposite of filter; returns multiple records
Blog.objects.order_by("created_at") - orders by created_date field
Blog.objects.order_by("-created_at") - reverses the order
Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") - performs a raw SQL query
Blog.objects.first().comments.all() - grabs all comments from the first Blog
Blog.objects.get(id=15).comments.first() - grabs the first comment from Blog id = 15
Comment.objects.get(id=15).blog.name - returns the name of the blog where Comment id = 15 belongs to

# This will return all the ninjas that belong to the Dojo with the id #8. "ninjas" is a ForeignKey related_name saved in the Ninja table, which is how the Dojo table can reference it.
Dojo.objects.get(id=8).ninjas.all().values()

#Relationships
# Create a variable to hold each individual query to help combine them.
a1 = Author.objects.get(id=1) #To check an item you need to traverse into the dictionary using index of 0 [0] and then dot notation of the specific collumn name. Ex: a1[0].name
b1 = Book.objects.get(id=1)
a1.books.add(b1) #Then, to create the relationship, connect it via the key (ManyToMany or Foreign) which is "books" in this example, and using the add() command.

# Conditions
You can do a more complicated search than just if a given field is equal to a given value. Instead of just passing in the field name as a keyword argument to .get, .filter, or .exclude, you'd pass the field name__lookup type (that's a double underscore, also known as a "dunder" for people on-the-go). 

For example

Admin.objects.filter(first_name__startswith="S") - filters objects with first_name that starts with "S"
Admin.objects.exclude(first_name__contains="E") - excludes objects where first_name contains "E"
Admin.objects.filter(age__gt=80)  - filters objects with age greater than 80


# Validation
1) Create a user.Manager class in your models.py file above your class. In the class create a function with all the validation logic (VALIDATION LOGIC SHOULD ONLY BE IN MODELS.PY FILE)
2) Place "objects = <ManagerClassName()>" in the class it is running validation on. 
3) Collect all error messages in a dictionary
4) Pass dictionary to the view where the function is being used
5) Check if there are any error messages in the dictionary using if: len < 0 else: run your query
6) Loop through your error messages dictionary and save the messages in messages (to flash messages) one message at a time.
7) In your HTML, loop through your messages and print them out.
8) Grab a beer!


# use this function to create users with validation
def create_valid_user():

    user = {}
    print "Enter a First Name"
    user['first_name'] = raw_input()

    print "Enter a Last Name"
    user['last_name'] = raw_input()

    print "Enter an Email Address"
    user['email'] = raw_input()

    print "Enter an Age"
    user['age'] = raw_input()

    User.objects.create(**user) # I'm unsure what the double splats are for, or if they are even neccessary. I think it had something to do with the kwargs validation that I removed.
    print "successfully created a user"

# This helper function prints variable or search query object data to the terminal so that you cn see what your selected object is. Returns them as separate statements, not as a single object.
#When creating a new function like this, don't forget to import the table at the top of the page.

def print_object_data(query):
    print query.first_name
    print query.last_name
    print query.email
    print query.age
