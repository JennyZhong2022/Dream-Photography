from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about,name='about'),

    path('photographers/', views.PhotographerList.as_view(),name='photographers_index'),
    path('photographers/create/',views.PhotographerCreate.as_view(),name='photographers_create'),
    path('photographers/<int:pk>/',views.PhotographerDetail.as_view(),
    name='photographers_details'),
    path('photographer/<int:pk>/assoc_client/<int:client_pk>/', views.AssocClientView.as_view(), name='assoc_client'),
    path('photographer/<int:pk>/unassoc_client/<int:client_pk>/', views.UnAssocClientView.as_view(), name='unassoc_client'),
    path('photographers/<int:pk>/update/',views.PhotographerUpdate.as_view(),name='photographers_update'),
    path('photographers/<int:pk>/delete/',views.PhotographerDelete.as_view(),name='photographers_delete'),


    path('clients/', views.ClientList.as_view(),name='clients_index'),
    path('clients/create/',views.ClientCreate.as_view(),name='clients_create'),
    path('clients/<int:pk>/',views.ClientDetail.as_view(),
    name='clients_details'),
    path('clients/<int:pk>/update/',views.ClientUpdate.as_view(),name='clients_update'),
    path('clients/<int:pk>/delete/',views.ClientDelete.as_view(),name='clients_delete'),

    # message from clients to photographers
    path('photographer/<int:photographer_pk>/send_message/<int:client_pk>/', views.SendMessageView.as_view(), name='send_message'),

    # sign up & login
    path('register/photographer/',views.register_photographer, name='register_photographer'),
    path('login/photographer/',views.login_photographer, name='login_photographer'),
    path('register/client/', views.register_client, name='register_client'),
    path('login/client/', views.login_client, name='login_client'),


]

