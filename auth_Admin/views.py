from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Connexion
from django.contrib.auth.models import User

DEFAULT_ADMIN_EMAIL = 'jktransadmin@gmail.com'
DEFAULT_ADMIN_PASSWORD = 'JKTransAdmin2026'

def connexion(request):
    if request.method == 'POST':
        form = Connexion(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            django_user = authenticate(request, username=email, password=mot_de_passe)
            if django_user is not None and django_user.is_active and (
                django_user.is_staff or django_user.is_superuser
            ):
                login(request, django_user)
                request.session['admininfo_id'] = django_user.id
                request.session['admininfo_email'] = django_user.email or django_user.username
                messages.success(request, 'Connexion réussie.')
                return redirect('Admin')
    else:
        form = Connexion()

    return render(request, 'auth_admin/login.html', {'form': form})


def logout_view(request):
    logout(request)
    request.session.pop('admininfo_id', None)
    request.session.pop('admininfo_email', None)
    messages.info(request, 'Vous avez bien été déconnecté.')
    return redirect('connexion')
