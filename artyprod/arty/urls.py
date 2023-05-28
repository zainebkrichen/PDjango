from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('a/', views.template, name='template'),
    path('home/', views.home, name='home'),

        
    path('register/', views.register,name="register"),
    
    path('ajoutProjet/', views.ajoutProjet, name='ajoutProjet'),
    path('listeProjets/', views.listeProjets, name='listeProjets'),
    path('modifierProjet/<int:projet_id>', views.modifierProjet,name="modifierProjet"),
    path('supprimerProjet/<int:projet_id>', views.supprimerProjet,name="supprimerProjet"),
    path('detail_projet/<int:projet_id>', views.detail_projet, name='detail_projet'),
    
    
    path('ajoutEquipe/', views.ajout_equipe, name='ajout_equipe'),
    path('listeEquipe/', views.listeEquipe ,name='listeEquipe' ),
    path('modifierEquipe/<int:pk>', views.modifierEquipe, name='modifierEquipe'),    
    path('supprimerEquipe/<int:pk>', views.supprimerEquipe, name="supprimerEquipe"),
    path('detailEquipe/<int:pk>', views.detailEquipe, name="detailEquipe"),
    
    path('add-person/', views.add_person, name='add_person'),
    path('person-list/', views.person_list, name='person_list'),
    
    path('contact/', views.contact, name='contact'),
    
]
