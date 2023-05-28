from django.http import HttpResponse
from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProjetForm, EquipeForm
from django.core.files.storage import default_storage
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetForm
from .models import Project
from .forms import ContactForm



# Create your views here.
def index(request):
    return HttpResponse("Première apllication django")
def home(request):
    return render(request,'arty/home.html')

def template(request):
    return render(request,'a.html')



# Create your views Projet.
def listeProjets(request):
    projets = Project.objects.all()
    return render(request, 'portfolio/listeProjets.html', {'projets': projets})


@login_required
def modifierProjet(request, projet_id):
    projet = get_object_or_404(Project, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.save()
            return redirect('listeProjets')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'portfolio/modifierProjet.html', {'form': form})


@login_required
def supprimerProjet(request, projet_id):
    projet = Project.objects.get(id=projet_id)
    projet.delete()
    return redirect('listeProjets')

@login_required
def ajoutProjet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listeProjets')
    else:
        form = ProjetForm()
    return render(request, 'portfolio/ajoutProjet.html', {'form': form})


@login_required
def detail_projet(request, projet_id):
    projet = Project.objects.get(id=projet_id)
    return render(request, 'portfolio/detail_projet.html', {'projet': projet})



# Create your views Equipe.
@login_required
def ajout_equipe(request):
    membres = Membre.objects.all()
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            form.personnel.set(request.POST.getlist('Membres'))
            return redirect('listeEquipe')
    else:
        form = EquipeForm()
    return render(request, 'equipe/ajoutEquipe.html', {'form': form, 'membres': membres})


@login_required
def listeEquipe(request):
    equipe_list = Equipe.objects.all()
    return render(request, 'equipe/listeEquipe.html', {'equipes': equipe_list})

@login_required
def supprimerEquipe(request, pk):
    equipe = Equipe.objects.get(id=pk)
    equipe.delete()
    return redirect('listeEquipe')

def detailEquipe(request, pk):
    equipe = Equipe.objects.get(id=pk)
    return render(request, 'equipe/detailEquipe.html',{'equipe':equipe})


@login_required
def modifierEquipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == "POST":
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            equipe = form.save(commit=False)
            equipe.save()
            messages.success(request, 'Equipe modifié avec succès!')
            return redirect('listeEquipe')
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'equipe/modifierEquipe.html', {'form': form})


#personne

@login_required
def add_person(request):
    if request.method == 'POST':
        form = MembreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = MembreForm()
    return render(request, 'personne/add_person.html', {'form': form})

@login_required
def person_list(request):
    persons = Membre.objects.all()
    return render(request, 'personne/person_list.html', {'persons': persons})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'arty/contact.html', {'form': form})




@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Enregistrement du fichier dans le stockage cloud
        path = default_storage.save('uploads/' + file.name, file)
        # Récupération de l'URL du fichier
        url = default_storage.url(path)
        return render(request, 'upload.html', {'url': url})
    return render(request, 'upload.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, f'Coucou , Votre compte a été créé avec succès !')
            # return render(request, 'registration/login.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("../a")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})


def logout(request):
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")