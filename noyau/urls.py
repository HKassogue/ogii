
from django.conf import settings
from django.urls import path
from noyau import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts',views.contacts,name="contacts"),
    path('',views.listerContacts,name="listerContacts"),
    path("connexion", views.connexion, name="connexion"),
    path("addContacts", views.ajouterContacts, name="ajouterContacts"),
]
