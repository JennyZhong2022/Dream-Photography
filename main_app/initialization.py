from django.contrib.auth.models import Group, Permission


def create_user_groups():
    # admin_group,_=Group.objects.get_or_create(name='Admin')
    photographer_group, _ = Group.objects.get_or_create(name='Photographer')
    client_group, _ = Group.objects.get_or_create(name='Client')