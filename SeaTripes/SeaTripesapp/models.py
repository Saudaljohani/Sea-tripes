from django.db import models

# Create your models here.

class Captain (models.Model):
    name_Captain=models.CharField(max_length=128)
    age_Captain=models.CharField(max_length=32)
    dec_Captain= models.TextField()
    avatar = models.ImageField(upload_to="images/")


class Trip(models.Model):
    titile=models.CharField(max_length=128)
    dec=models.TextField()
    date=models.DateTimeField()
    pic = models.ImageField(upload_to="images/")