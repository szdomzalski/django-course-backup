from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # image = models.FileField(upload_to='images', max_length=128)
    image = models.ImageField(upload_to='images', max_length=128)
