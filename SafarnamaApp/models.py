from django.db import models
from django.contrib.auth.models import User

class super(models.Model):
    city = models.CharField(max_length=100, default=None)
    hotel = models.CharField(max_length=100, default=None)
    tax = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
    off = models.IntegerField(default=None)
    rating = models.IntegerField( default=None)
    price = models.IntegerField()
    delete = models.IntegerField()
    img1 = models.ImageField(upload_to='pics', default=None)
    img2 = models.ImageField(upload_to='pics', default=None)
    img3 = models.ImageField(upload_to='pics', default=None)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='pics')
