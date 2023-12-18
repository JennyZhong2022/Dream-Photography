from django.urls import path
from . import views

urlpatterns=[
  path('',views.home, name='home'),
  path('about/',views.about,name='about'),

  path('photographers/', views.PhotographerList.as_view(),name='photographers_index'),
  path('photographers/create',views.PhotographerCreate.as_view(),name='photographers_create'),
  path('photographers/<int:pk>',views.PhotographerDetail.as_view(),
  name='photographers_details'),
  path('photographers/<int:pk>/update/',views.PhotographerUpdate.as_view(),name='photographers_update'),
  path('photographers/<int:pk>/delete/',views.PhotographerDelete.as_view(),name='photographers_delete'),






]

