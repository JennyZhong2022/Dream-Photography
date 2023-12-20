from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

Expertise=(
  ('WP','Wedding Photography'),
  ('WV','Wedding Videography'),
  ('WB','Wedding Photography & Videography'),
  ('PP','PreWedding Photography'),
  ('PV','PreWedding Videography'),
  ('PB','PreWedding Photography & Videography'),
  ('AL','All-round')
)



class Client(models.Model):
    bride_name = models.CharField(max_length=50)
    groom_name = models.CharField(max_length=50)
    bride_age = models.IntegerField()
    groom_age = models.IntegerField()
    # Wedding Date will be default show on the page
    wedding_date = models.DateField('Wedding Date')
    location = models.CharField(max_length=250)
    guests = models.IntegerField()  
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.bride_name} and {self.groom_name}'s Wedding"



    def get_absolute_url(self):
      return reverse('clients_details',kwargs={'pk':self.id})  


class Photographer(models.Model):
  name=models.CharField(max_length=50)
  area_of_expertise=models.CharField(
    max_length=2, 
    choices=Expertise,
    default=Expertise[0][0]
    )
  description=models.TextField(max_length=250)
  clients=models.ManyToManyField(Client)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} :{self.get_area_of_expertise_display()}'

  def get_absolute_url(self):
    return reverse('photographers_details',kwargs={'pk':self.id})  

class Message(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='received_messages')
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f'Message from{self.sender} to {self.recipient}'