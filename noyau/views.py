from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.db import models
from .forms import CreerContactsForm


def listerContacts(request):
    from django.http import Http404
    contacts = Contacts.objects.all()
    #auteurs = Auteur.objects.all()

    context = {'contacts': contacts}

    return render(request, "noyau/listerContacts.html", context)

def ajouterContacts(request):
    from django.http import Http404
    if request.method == 'POST':
        form = CreerContactsForm()
        form= CreerContactsForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'noyau/ajouterContacts.html')
