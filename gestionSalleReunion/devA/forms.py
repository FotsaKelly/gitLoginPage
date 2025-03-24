from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Arbre
import datetime

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fonction = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'fonction']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'fonction')

class ArbreForm(forms.ModelForm):
    class Meta:
        model = Arbre
        fields = '__all__'
        widgets = {
            'date_Reunion': forms.DateInput(attrs={'type': 'date'}),
            'heure_Debut': forms.TimeInput(attrs={'type': 'time'}),
            'duree': forms.TextInput(attrs={'placeholder': 'Durée en heures'}),  # Placeholder pour la durée
        }

    def clean_heure_Debut(self):
        heure_Debut = self.cleaned_data.get('heure_Debut')
        if heure_Debut and heure_Debut.hour < 8:
            raise forms.ValidationError("L'heure de début ne peut pas être avant 8 heures.")
        return heure_Debut

    def clean_date_Reunion(self):
        date_Reunion = self.cleaned_data.get('date_Reunion')
        if date_Reunion and date_Reunion < datetime.date.today():
            raise forms.ValidationError("La date de réunion ne peut pas être dans le passé.")
        return date_Reunion

    def save(self, commit=True):
        arbre = super().save(commit=False)
        if commit:
            arbre.save()
        return arbre
