from django.contrib import admin
from .models import Photographer,Client
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.contrib import messages

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Client)

class MyAdminSite(admin.AdminSite):
    def login(self, request, extra_context=None):
        # Redirect photographers from the admin login page
        if request.method == 'POST':
            username = request.POST.get('username')
            user = User.objects.filter(username=username).first()
            if user and user.groups.filter(name='Photographer').exists():
                messages.error(request, "Photographers cannot log in here.")
                return redirect('photographer_login')  # Redirect to photographer login
        return super().login(request, extra_context)

admin.site = MyAdminSite()