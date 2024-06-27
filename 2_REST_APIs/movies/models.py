from django.db import models

# Create your models here.

class Moviedata(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    duration = models.IntegerField() # in minutes
    rating = models.FloatField() 
    genre = models.CharField(max_length=100, default='action')
    image = models.ImageField(upload_to='Images/', default='Images/None/no-img.jpg')