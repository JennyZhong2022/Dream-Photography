from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic import ListView, DetailView
from .models import Photographer,Client

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')  

class PhotographerList(ListView):
  model=Photographer  


class PhotographerDetail(DetailView):
  model=Photographer  

class PhotographerCreate(CreateView):
  model = Photographer
  fields = '__all__'  

class PhotographerUpdate(UpdateView):
  model=Photographer
  fields=['area_of_expertise','description']

class PhotographerDelete(DeleteView):
  model=Photographer
  success_url='/photographers'




class ClientList(ListView):
  model=Client  


class ClientDetail(DetailView):
  model=Client  

class ClientCreate(CreateView):
  model = Client
  fields = '__all__'  

class ClientUpdate(UpdateView):
  model=Client
  fields=['bride_age','groom_age','wedding_date','location','guests'] 

class ClientDelete(DeleteView):
  model=Client
  success_url='/clients'
