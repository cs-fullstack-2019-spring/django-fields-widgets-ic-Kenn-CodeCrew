from django.db import models



# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=200, default=0)
    password = models.CharField(max_length=200, default=0)
    date = models.DateField(default="")
    email = models.EmailField(default="")
    booleanItem = models.BooleanField()
    radio = models.CharField(max_length=200)
    dropDown = models.CharField(max_length=200)#, choices=yesNo)
    checkbox = models.CharField(max_length=200)
