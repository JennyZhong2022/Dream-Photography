from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic import ListView, DetailView
from .models import Photographer

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
