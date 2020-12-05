from django.db import models
from django.db.models import Model

# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)

class Contribute(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    link = models.URLField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name
