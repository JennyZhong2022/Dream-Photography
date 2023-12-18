from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

class Photographer(models.Model):
  name=models.CharField(max_length=50)
  area_of_expertise=models.CharField(max_length=50)
  description=models.TextField(max_length=250)

  def __str__(self):
    return f'{self.name}'

  def get_absolute_url(self):
    return reverse('photographers_details',kwargs={'pk':self.id})  

