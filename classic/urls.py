from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('Apropos/', views.about, name='apropos'),
    path('Contact/', views.contact, name='contact'),
    path('Catalogue/', views.cars, name='cars'),
    path('Services/', views.services, name='service'),
    path('Details/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('Forfaits/', views.forfait, name='forfait'),
]
