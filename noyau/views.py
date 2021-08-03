from django.shortcuts import render
from noyau.models import Contacts


def contacts(request):
    
    return render(request,'noyau/index.html')