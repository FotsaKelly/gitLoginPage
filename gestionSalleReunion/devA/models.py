from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    fonction = models.CharField(max_length=50, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='devA_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='devA_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Arbre(models.Model):
    nature_Reunion = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    nom_Salle = models.CharField(max_length=100)
    date_Reunion = models.DateField()
    heure_Debut = models.TimeField()
    duree = models.DurationField()
    capacite_Salle = models.IntegerField(default=0)  # Changer en IntegerField
    nombre_participants = models.IntegerField(default=0)
    nom_Ville = models.CharField(max_length=100)  # Changer en CharField
    nom_Site = models.CharField(max_length=100)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arbres')
    statut = models.BooleanField(default=False, null=True)
    valided = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.titre
