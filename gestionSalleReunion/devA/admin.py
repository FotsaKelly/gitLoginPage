from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Arbre
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'email', 'fonction', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'fonction')
    ordering = ('username',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'fonction'),
        }),
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal info', {
            'fields': ('fonction',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(User, UserAdmin)

class ArbreAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nature_Reunion', 'titre', 'nom_Salle', 'date_Reunion', 
        'heure_Debut', 'duree', 'capacite_Salle', 'nombre_participants', 
        'nom_Ville', 'nom_Site', 'utilisateur_email'
    )

    list_filter = ('date_Reunion', 'nom_Ville', 'nom_Site')
    search_fields = ('titre', 'nom_Salle', 'nom_Ville', 'nom_Site')

    fieldsets = (
        (None, {
            'fields': (
                'nature_Reunion', 'titre', 'nom_Salle', 'date_Reunion', 
                'heure_Debut', 'duree', 'capacite_Salle', 'nombre_participants', 
                'nom_Ville', 'nom_Site', 'utilisateur'
            )
        }),
    )

    def utilisateur_email(self, obj):
        return obj.utilisateur.email
    utilisateur_email.short_description = 'Email Utilisateur'

admin.site.register(Arbre, ArbreAdmin)
