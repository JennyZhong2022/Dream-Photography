from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about,name='about'),
 
    # photographers
    path('photographers/', views.PhotographerList.as_view(),name='photographers_index'),
    path('photographers/create/',views.PhotographerCreate.as_view(),name='photographers_create'),
    path('photographers/<int:pk>/',views.PhotographerDetail.as_view(),
    name='photographers_details'),
    path('photographer/<int:pk>/assoc_client/<int:client_pk>/', views.AssocClientView.as_view(), name='assoc_client'),
    path('photographer/<int:pk>/unassoc_client/<int:client_pk>/', views.UnAssocClientView.as_view(), name='unassoc_client'),
    path('photographers/<int:pk>/update/',views.PhotographerUpdate.as_view(),name='photographers_update'),
    path('photographers/<int:pk>/delete/',views.PhotographerDelete.as_view(),name='photographers_delete'),

    # photos for photographers
    path('photographers/<int:photographer_id>/gallery/',views.photographer_gallery, name='photographers_gallery'),
    path('photographers/<int:photographer_id>/add_photo/',views.add_photo,name='add_photo'),
    

    # album photos from photographer to client
    path('photographers/<int:photographer_id>/client_album/<int:client_id>/', views.client_album,name='client_album'),
    path('photographers/<int:photographer_id>/client_album/<int:client_id>/add_photo/', views.add_photo, name='client_add_photo'), 

    # album photos received by client
    path('clients/<int:client_id>/client_album/', views.client_received_album, name='client_received_album'),
    # album photos can be downloaded by client
    path('clients/client_album_download_photo/<int:photo_id>/', views.download_photo, name='download_photo'),

    


    # delete photos from photographer gallery
    path('delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),
   
    # delete photos from client album by photographer
    path('delete_photo/<int:photo_id>/<int:client_id>/', views.delete_photo, name='delete_album_photo'),
    

    # clients
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
    path('register/admin/',views.register_admin, name='register_admin'),
    path('login/admin/',views.login_admin, name='login_admin'),
    


]

