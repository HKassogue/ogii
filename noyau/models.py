from django.db import models

class Contacts(models.Model):
    tel_portable = models.CharField(max_length=50)
    tel_domicile = models.CharField(max_length=50)
    tel_bureau = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

# Create your models here.
