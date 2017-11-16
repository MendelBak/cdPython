

c

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

# Many to Many: Many Products Many Orders
class Product2(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  orders = models.ManyToManyField(Order, related_name = 'products')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)


  # Many to Many Relationships

  # Query for a single product and order
  order1 = Order.objects.get(id=1)
  product1 = Product2.objects.get(id=1)

  # Add product into order
  order1.products.add(product1)

  # See all products in an order
  order1.products.all()