from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Candidato, Voto, Usuario
from django.contrib.auth.models import User

#User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario', max_length=254)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class VotoForm(forms.ModelForm):
    class Meta:
        model = Voto
        fields = ['candidato']

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
           user.save()
        return user

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nombre', 'partido', 'descripcion', 'foto']