from django.contrib import admin
from .models import Photographer,Client
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.contrib import messages

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Client)
