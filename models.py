
# virtual_trail/models.py
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional customer-related fields like sizes, preferences, etc.
    sizes = models.CharField(max_length=255)
    # ...

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    sizes_available = models.CharField(max_length=255)
    # ...

class VirtualTrailSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    selected_size = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed
class VirtualTrailRoom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
