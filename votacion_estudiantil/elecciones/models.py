from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#User = get_user_model()

class Usuario(AbstractUser):
    es_estudiante = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    pass
    
class Candidato(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    partido = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='candidatos/', default='candidatos/user.png')

    def __str__(self):
        return self.nombre

class Voto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} votó por {self.candidato.nombre}"
    
class Resultado(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    votos = models.IntegerField(default=0)
