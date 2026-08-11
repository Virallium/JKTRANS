from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import Connexion
from .models import Admininfo

DEFAULT_ADMIN_EMAIL = 'jktransadmin@gmail.com'
DEFAULT_ADMIN_PASSWORD = 'JKTransAdmin2026'

def connexion(request):
    if request.method == 'POST':
        form = Connexion(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            admin_user = Admininfo.objects.filter(email__iexact=email).first()
            if admin_user is None and Admininfo.objects.count() == 0 and email.lower() == DEFAULT_ADMIN_EMAIL:
                admin_user = Admininfo.objects.create(
                    email=DEFAULT_ADMIN_EMAIL,
                    mot_de_passe=make_password(DEFAULT_ADMIN_PASSWORD),
                )

            if admin_user is None or not admin_user.check_password(mot_de_passe):
                form.add_error(None, 'Email ou mot de passe incorrect.')
            else:
                request.session['admininfo_id'] = admin_user.id
                request.session['admininfo_email'] = admin_user.email
                messages.success(request, 'Connexion réussie.')
                return redirect('Admin')
    else:
        form = Connexion()

    return render(request, 'auth_admin/login.html', {'form': form})


def logout_view(request):
    request.session.pop('admininfo_id', None)
    request.session.pop('admininfo_email', None)
    messages.info(request, 'Vous avez bien été déconnecté.')
    return redirect('connexion')
