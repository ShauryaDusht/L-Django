from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# we want to create a model for the food app
# model is nothing but a class that represents a table in the database
# each class attribute represents a column in the table

class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30) # name column in the table
    description = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=5, decimal_places=2) 
    image = models.CharField(max_length=500, default='') 
    # if we want establish connection between 2 model then we can use ForeignKey
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # post owner is the user who created the post
    

    # reverse will redirect to the detail page of the post
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    