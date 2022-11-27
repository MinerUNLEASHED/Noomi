from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserMoreInfo(models.Model):
    user = models.OneToOneField(User)
    
    # portfolio_site = models.URLField(blank=True) #Means User Doesn't Have To Fill It Out
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    
    
    def __str__(self):
        return self.user.username