
# <!-- THIS IS FROM VANESSA'S GIST FROM THE LECTURE -->

from __future__ import unicode_literals

from django.db import models


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

# One to Many: 1 User Many Orders
class Order(models.Model):
  total_cost = models.IntegerField()
  user = models.ForeignKey(User, related_name = 'orders')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)


class Product2Manager(models.Manager):
  # Adding validations
  # Product name must be greater than 2 characters
  # Price must be an int over $1
  def create_product_validator(self, postData):
    print "POST DATA IN MANAGER"
    print postData
    
    errors = {}
    
    
    if len(postData['name']) < 2:
      # Creating new key value pair in errors dictionary
      errors['name'] = 'Name must be over 2 characters'

    # Check if price exists
    if postData['price']:
      if not isinstance(int(postData['price']), int):
        errors['price_numbers'] = 'Price must be numbers only'

      if not int(postData['price']) > 0:
        errors['price_value'] = 'Price must be over 0'
    else:
      errors['price'] = 'Price cannot be blank'

    return errors


# Many to Many: Many Products Many Orders
class Product2(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  orders = models.ManyToManyField(Order, related_name = 'products')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  objects = Product2Manager()