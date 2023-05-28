from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')

    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id','nom', 'description', 'image', 'temoignage']

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ('name', 'cv', 'image', 'linkedin')
        
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'
        

        
class ContactForm(forms.ModelForm):
      class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'