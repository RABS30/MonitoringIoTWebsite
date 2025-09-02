from django.db import models
from django.contrib.auth.models import AbstractUser

class authUser(AbstractUser):
    email = models.EmailField(("Email"),unique=True, max_length=254)    
    
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    