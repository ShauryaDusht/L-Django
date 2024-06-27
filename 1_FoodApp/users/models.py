from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # on_delete means if user is deleted, delete the profile
    image = models.ImageField(default='defaultPFP.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100, default='Location')
    
    def __str__(self):
        return f'{self.user.username} Profile'