from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic import ListView, DetailView
from .models import Photographer,Client,Message
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')  

class PhotographerList(LoginRequiredMixin,ListView):
    model=Photographer  


class PhotographerDetail(LoginRequiredMixin,DetailView):
    model=Photographer  

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context dictionary.
        context = super().get_context_data(**kwargs)

        # Retrieve the Photographer instance that the view is displaying.
        photographer = self.get_object()

        # Add the photographer's associated clients to the context.
        context['clients'] = photographer.clients.all()

        messages = Message.objects.filter(recipient=photographer).select_related('sender')
        context['messages'] = messages

        # Get all clients not currently associated with this photographer.
        # It excludes clients already linked to the photographer.
        all_clients = Client.objects.exclude(id__in=photographer.clients.all())

        # Add these available clients to the context.
        context['all_clients'] = all_clients
        return context


class AssocClientView(LoginRequiredMixin,View):
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

class UnAssocClientView(LoginRequiredMixin,View):
     def post(self, request, pk, client_pk):
        photographer = get_object_or_404(Photographer, pk=pk)
        client = get_object_or_404(Client, pk=client_pk)
        photographer.clients.remove(client)
        return redirect(reverse('photographers_details', kwargs={'pk': pk}))



class PhotographerCreate(LoginRequiredMixin,CreateView):
    model = Photographer
    fields = ['name','area_of_expertise','description']
    
class PhotographerUpdate(LoginRequiredMixin,UpdateView):
    model=Photographer
    fields=['area_of_expertise','description']

class PhotographerDelete(LoginRequiredMixin,DeleteView):
    model=Photographer
    success_url='/photographers'




class ClientList(LoginRequiredMixin,ListView):
    model=Client  
    # if the user is in group client, only can see own list
    # else user can see all list
    def get_queryset(self):
        """Return the list of items for this view."""
        if self.request.user.groups.filter(name='Client').exists():
            # If the user is in the 'Client' group, show only their entries
            return Client.objects.filter(user=self.request.user)
        else:
            # Otherwise, show all entries
            return Client.objects.all()  



class ClientDetail(LoginRequiredMixin,DetailView):
    model=Client 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        context['photographers'] = client.photographer_set.all()
        all_photographers = Photographer.objects.all()
        context['all_photographers'] = all_photographers
      

        return context


class ClientCreate(LoginRequiredMixin,CreateView):
    model = Client
    fields=['bride_name','groom_name','bride_age','groom_age','wedding_date','location','guests'] 

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the client
    # Let the CreateView do its job as usual
        return super().form_valid(form)


class ClientUpdate(LoginRequiredMixin,UpdateView):
    model=Client
    fields=['bride_name','groom_name','bride_age','groom_age','wedding_date','location','guests'] 

class ClientDelete(LoginRequiredMixin,DeleteView):
    model=Client
    success_url='/clients'


class SendMessageView(LoginRequiredMixin,View):
    def post(self, request, client_pk, photographer_pk):
        photographer = get_object_or_404(Photographer, pk=photographer_pk)
        client = get_object_or_404(Client, pk=client_pk)

        content = request.POST.get('content')
        Message.objects.create(sender=client, recipient=photographer, content=content)

        
        success_message = f'Your message has been sent to {photographer.name}'
        messages.success(request,success_message)
            # Redirect to the appropriate page, client details or another relevant page
        return redirect(reverse('clients_details', kwargs={'pk': client_pk}))
        
 
#  GROUP photographer
                
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1','password2']



def register_photographer(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group=Group.objects.get(name='Photographer')
            user.groups.add(group)
            login(request, user)
            return redirect('photographers_index')
    else:
        form=RegistrationForm()
    return render(request,'registration/photographer_register.html',{'form':form})    


def login_photographer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Check if user is a photographer and not a client
        if user is not None and user.groups.filter(name='Photographer').exists() and not user.groups.filter(name='Client').exists():
            login(request, user)
            return redirect('photographers_index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/photographer_login.html')


#  GROUP client


# views.py

def register_client(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Reusing the same form
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Client')
            user.groups.add(group)
            login(request, user)
            return redirect('clients_index')  # Redirect to a client-specific page
    else:
        form = RegistrationForm()

    return render(request, 'registration/client_register.html', {'form': form})

def login_client(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Check if user is a client and not a photographer
        if user is not None and user.groups.filter(name='Client').exists() and not user.groups.filter(name='Photographer').exists():
            login(request, user)
            return redirect('clients_index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/client_login.html')
