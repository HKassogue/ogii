from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.db import models
from .forms import CreerContactsForm

def connexion(request):
    from .forms import ConnectForm
    form = ConnectForm(request.POST or None)
    erreur = False
    if form.is_valid():
        username = form.cleaned_data["login"]
        password = form.cleaned_data["m_pass"]
        from django.contrib.auth import authenticate, login
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(listerContacts)
        else:
            erreur = True
    return render(request, "noyau/connexion.html", locals())
def contacts(request,id=1):
    from django.http import Http404
    if id<1:
        raise Http404
    else:
        from .models import Contacts
        lignes = Contacts.objects.filter(id=id)
    return render(request, "noyau/contacts.html", locals())

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
