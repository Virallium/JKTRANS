from django import forms

class Connexion(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Votre adresse email',
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
    