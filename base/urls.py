from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'), 
    path('contacts', views.contacts, name='contacts'),
    path('send/<str:pk>/email', views.sendEmail, name='sendmail'),
    path('tracking/details/', views.tracking_details, name='track-details'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add/client', views.addClient, name='add-client'),
    path('add/<str:pk>/item', views.addItem, name='add-items'),
    path('edith/<str:pk>/client', views.edit, name="edit"), 
    path('edith/<str:pk>/item', views.editItem, name="edit-item"),
    path('delete/<str:pk>/client', views.delete, name='delete'),
    path('delete/<str:pk>/item', views.deleteItem, name='delete-item'),
]