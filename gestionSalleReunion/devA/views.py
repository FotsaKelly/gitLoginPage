from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ArbreForm
from .models import Arbre

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'devA/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('arbre_list')
        else:
            messages.error(request, 'Nom d\'utilisateur ou Mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'devA/connexion.html', {'form': form})

def acceuil(request):
    return render(request, 'devA/acceuil.html')

@login_required
def arbre_list(request):
    arbres = Arbre.objects.filter(statut=False)
    return render(request, 'devA/arbre_list.html', {'arbres': arbres})






@login_required
def arbre_list_admin_validated(request):
    arbres = Arbre.objects.filter(valided=True)
    return render(request, 'devA/arbre_list_valided.html', {'arbres': arbres})


@login_required
def arbre_list_admin_non_validated(request):
    arbres = Arbre.objects.filter(valided=False, statut=True)
    return render(request, 'devA/arbre_list_rejected.html', {'arbres': arbres})

@login_required
def arbre_detail(request, pk):
    arbre = get_object_or_404(Arbre, pk=pk)
    return render(request, 'devA/arbre_detail.html', {'arbre': arbre})

@login_required
def arbre_create(request):
    if request.method == 'POST':
        form = ArbreForm(request.POST)
        if form.is_valid():
            arbre = form.save(commit=False)
            arbre.utilisateur = request.user  # Assigner l'utilisateur connecté
            arbre.save()
            return redirect('arbre_list')
    else:
        form = ArbreForm()
    return render(request, 'devA/arbre_form.html', {'form': form})

@login_required
def arbre_valider(request, pk):
    arbre = Arbre.objects.get(id=pk)
    arbre.statut = True
    arbre.valided = True
    arbre.save()
    return redirect('arbre_list')

@login_required
def arbre_delete(request, pk):
    arbre = Arbre.objects.get(id=pk)
    arbre.statut = True
    arbre.valided = False
    arbre.save()
    return redirect('arbre_list')
