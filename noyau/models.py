from django.db import models

# Create your models here.
class Personne(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Profession = models.CharField(max_length=30)
class Description(models.Model):
    Taille = models.IntegerField()
    Teint = models.CharField(max_length=30)
    Cheveux = models.CharField(max_length=30)
    Photo = models.CharField(max_length=30)
    Empreinte = models.CharField(max_length=30)
    Signature = models.CharField(max_length=30)
class ActedeNaissance(models.Model):
    Num = models.CharField(max_length=30)
    Date = models.DateField()
    Addresse = models.CharField(max_length=30)
    Date_Edition = models.DateField()
    Signataire = models.ForeignKey(Personne, on_delete = models.CASCADE)
    