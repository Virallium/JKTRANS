from django import forms

class Connexion(forms.Form):
    email = forms.CharField(
        label='Identifiant ou adresse email',
        widget=forms.TextInput(attrs={
            'placeholder': 'Votre identifiant ou adresse email',
            'class': 'form-input',
            'id': 'email',
        })
    )
    mot_de_passe = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Votre mot de passe',
            'class': 'form-input',
            'id': 'mot_de_passe',
        })
    )
    