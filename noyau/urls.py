
from django.conf import settings
from django.urls import path
from noyau import views

urlpatterns = [
    
    path('contacts/',views.contacts,name="contacts")
]
