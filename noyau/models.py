from django.db import models

class Contact(models.Model):
    tel_portable = models.CharField(max_length=30)
    tel_bureau = models.CharField(max_length=30)
    tel_domicile = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
