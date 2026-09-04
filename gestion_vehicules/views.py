from functools import wraps

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import ChauffeurForm, VehiculeForm
from .models import Vehicule, Chauffeur


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('admininfo_id') or (
            request.user.is_authenticated and request.user.is_staff
        ):
            return view_func(request, *args, **kwargs)
        messages.error(request, 'Veuillez vous connecter pour accéder à cette page.')
        return redirect('Admin')

    return _wrapped_view


@admin_required
def Admin(request):
    vehicules = Vehicule.objects.all()
    chauffeurs = Chauffeur.objects.all()
    return render(request, 'admin/Admin.html', {'vehicules': vehicules, 'chauffeurs': chauffeurs})


@admin_required
def vehicule_create(request):
    if request.method == 'POST':
        form = VehiculeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Véhicule ajouté avec succès.')
            return redirect('Admin')
    else:
        form = VehiculeForm()
    return render(request, 'admin/vehicule_form.html', {'form': form, 'title': 'Ajouter un véhicule'})


@admin_required
def vehicule_update(request, pk):
    vehicule = Vehicule.objects.get(pk=pk)
    if request.method == 'POST':
        form = VehiculeForm(request.POST, request.FILES, instance=vehicule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Véhicule mis à jour avec succès.')
            return redirect('Admin')
    else:
        form = VehiculeForm(instance=vehicule)
    return render(request, 'admin/vehicule_form.html', {'form': form, 'title': 'Modifier un véhicule'})


@admin_required
def vehicule_delete(request, pk):
    vehicule = Vehicule.objects.get(pk=pk)
    vehicule.delete()
    messages.success(request, 'Véhicule supprimé avec succès.')
    return redirect('Admin')


@admin_required
def chauffeur_create(request):
    if request.method == 'POST':
        form = ChauffeurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chauffeur ajouté avec succès.')
            return redirect('Admin')
    else:
        form = ChauffeurForm()
    return render(request, 'admin/chauffeur_form.html', {'form': form, 'title': 'Ajouter un chauffeur'})


@admin_required
def chauffeur_update(request, pk):
    chauffeur = Chauffeur.objects.get(pk=pk)
    if request.method == 'POST':
        form = ChauffeurForm(request.POST, instance=chauffeur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chauffeur mis à jour avec succès.')
            return redirect('Admin')
    else:
        form = ChauffeurForm(instance=chauffeur)
    return render(request, 'admin/chauffeur_form.html', {'form': form, 'title': 'Modifier un chauffeur'})


@admin_required
def chauffeur_delete(request, pk):
    chauffeur = Chauffeur.objects.get(pk=pk)
    chauffeur.delete()
    messages.success(request, 'Chauffeur supprimé avec succès.')
    return redirect('Admin')


