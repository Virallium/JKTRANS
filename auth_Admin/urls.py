from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.connexion,name="connexion"),
    path('Logout', views.logout_view, name='deconnexion'),
]
