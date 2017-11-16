


# <!-- THIS IS FROM VANESSA'S GIST FROM THE LECTURE -->

from django.shortcuts import render, redirect
from .models import Product2
from django.contrib import messages

def index(request):
  
  if not 'total' in request.session:
    request.session['total'] = 0
  
  try: 
    request.session['products']
  except KeyError:
     request.session['products'] = 0

  all_products = Product2.objects.all() # -> []
  # Product2.objects.get(name="Gucci Purse", price = 4000)  -> {}
  # Product2.objects.filter(name="Gucci Purse")  -> []

  context = {
    'products': all_products
  }

  return render(request, 'new_app/index.html' , context)

def checkout(request):
  return render(request, 'new_app/checkout.html')

def buy_products(request):
  request.session['price'] = request.POST['price']
  request.session['total'] = request.session['total'] + (int(request.POST['price']) * int(request.POST['quantity']))
  request.session['products'] = int(request.session['products']) + int(request.POST['quantity'])

  return redirect('/amadon/checkout')

def add_product(request):
  errors = Product2.objects.create_product_validator(request.POST)

  # If errors dictionary is empty
    # Add to DB
  # Else set flash messages
  if len(errors) <= 0:
    new_name = request.POST['name']
    new_price = int(request.POST['price'])
    Product2.objects.create(name = new_name, price = new_price)
  else:
    for x in errors:
      # save each error into messages seperately
      messages.error(request, errors[x])
  

  return redirect('/amadon')

