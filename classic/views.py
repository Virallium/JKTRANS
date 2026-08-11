from django.shortcuts import render
from django.db.models import Q
from gestion_vehicules.models import Vehicule
def home(request):
    search_query = request.GET.get('car_model', '').strip()
    vehicules_catalogue = Vehicule.objects.all()
    if search_query:
        vehicules_catalogue = vehicules_catalogue.filter(
            Q(marque__icontains=search_query) | Q(modele__icontains=search_query)
        )
    vehicules_A_la_une = vehicules_catalogue[:6]
    return render(request, 'pages/home.html', {'cars': vehicules_A_la_une})

def about(request):
    return render(request, 'pages/apropos.html')
def contact(request):
    return render(request, 'pages/contact.html')
def cars(request):
    search_query = request.GET.get('q', '').strip() or request.GET.get('car_model', '').strip()
    brand_query = request.GET.get('brand', '').strip()

    vehicules_catalogue = Vehicule.objects.all()

    if brand_query:
        brand_norm = brand_query.strip()
        vehicules_catalogue = vehicules_catalogue.filter(marque__iexact=brand_norm)

    if search_query:
        vehicules_catalogue = vehicules_catalogue.filter(
            Q(marque__icontains=search_query) | Q(modele__icontains=search_query)
        )

    brands = Vehicule.objects.order_by('marque').values_list('marque', flat=True).distinct()
    return render(request, 'pages/cars.html', {
        'cars': vehicules_catalogue,
        'brands': brands,
        'selected_brand': brand_query,
    })

def services(request):
    return render(request, 'pages/service.html')
def vehicle_detail(request, pk):
    vehicule = Vehicule.objects.get(pk=pk)
    return render(request, 'pages/details_car.html', {'vehicule': vehicule})
def forfait(request):
    return render(request, 'pages/forfait.html')