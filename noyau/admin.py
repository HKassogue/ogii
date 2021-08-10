from django.contrib import admin
from  .models import Contacts

@admin.register(Contacts)
class Contacts(admin.ModelAdmin):

   list_display=('tel_portable','tel_domicile','tel_bureau','email')


# Register your models here.
