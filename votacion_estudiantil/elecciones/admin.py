from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Candidato, Voto, Usuario

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'partido', 'descripcion')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'partido')  # Campos para buscar

@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'candidato', 'fecha')
    search_fields = ('usuario', 'candidato')
    
class UsuarioAdmin(UserAdmin):
    model = Usuario
    # Define los campos que se mostrarán en el admin
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Usuario, UsuarioAdmin)