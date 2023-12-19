from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic import ListView, DetailView
from .models import Photographer,Client
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View




# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')  

class PhotographerList(ListView):
    model=Photographer  


class PhotographerDetail(DetailView):
    model=Photographer  

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context dictionary.
        context = super().get_context_data(**kwargs)

        # Retrieve the Photographer instance that the view is displaying.
        photographer = self.get_object()

        # Add the photographer's associated clients to the context.
        context['clients'] = photographer.clients.all()

        # Get all clients not currently associated with this photographer.
        # It excludes clients already linked to the photographer.
        all_clients = Client.objects.exclude(id__in=photographer.clients.all())

        # Add these available clients to the context.
        context['all_clients'] = all_clients
        return context


class AssocClientView(View):
    # Define a POST method for this view.
    def post(self, request, pk, client_pk):
        # Retrieve the photographer and client objects, ensuring they exist.
        # If not, a 404 error page will be raised.
        photographer = get_object_or_404(Photographer, pk=pk)
        client = get_object_or_404(Client, pk=client_pk)

        # Associate the client with the photographer.
        photographer.clients.add(client)

        # Redirect to the photographer's detail page after the association.
        return redirect(reverse('photographers_details', kwargs={'pk': pk}))


class PhotographerCreate(CreateView):
    model = Photographer
    fields = ['name','area_of_expertise','description']

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
