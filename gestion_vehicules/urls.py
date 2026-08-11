from django.urls import path
from . import views

urlpatterns = [
    path('gestion/', views.Admin, name='Admin'),
    path('gestion/vehicules/ajouter/', views.vehicule_create, name='vehicule_create'),
    path('gestion/vehicules/<int:pk>/modifier/', views.vehicule_update, name='vehicule_update'),
    path('gestion/vehicules/<int:pk>/supprimer/', views.vehicule_delete, name='vehicule_delete'),
    path('gestion/chauffeurs/ajouter/', views.chauffeur_create, name='chauffeur_create'),
    path('gestion/chauffeurs/<int:pk>/modifier/', views.chauffeur_update, name='chauffeur_update'),
    path('gestion/chauffeurs/<int:pk>/supprimer/', views.chauffeur_delete, name='chauffeur_delete'),
]
