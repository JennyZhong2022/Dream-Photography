# Generated by Django 5.0 on 2023-12-18 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_clients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]