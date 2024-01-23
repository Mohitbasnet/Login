from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you need
    # For example: profile_picture = models.ImageField(upload_to='profile_pics/')
    pass
