from django.db import models


class Contacts(models.Model):
    tel_portable = models.CharField(max_length=50)
    tel_domicile = models.CharField(max_length=50)
    tel_bureau = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
      verbose_name = "contacts"
    def __str__(self):
     return "({0}, {1}, {2},{3},{})".format(self.id,self.tel_portable, self.tel_domicile,self.tel_bureau,self.email)


# Create your models here.
