from django import forms
from .models import Chauffeur, Vehicule


class ChauffeurForm(forms.ModelForm):
    class Meta:
        model = Chauffeur
        fields = ['nom', 'prenom', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['marque', 'modele', 'annee', 'couleur', 'prix', 'image', 'plaque', 'nombre_siege', 'Chauffeur']
        widgets = {
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'modele': forms.TextInput(attrs={'class': 'form-control'}),
            'annee': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'couleur': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'plaque': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_siege': forms.NumberInput(attrs={'class': 'form-control'}),
            'Chauffeur': forms.Select(attrs={'class': 'form-control'}),
        }
