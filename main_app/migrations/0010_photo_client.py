# Generated by Django 5.0 on 2023-12-21 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.client'),
        ),
    ]
