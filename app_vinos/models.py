from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Vino(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)  # Tinto, Blanco, Rosado, etc.
    anio = models.IntegerField()  # Año de producción
    bodega = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Preferencia(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_vino = models.CharField(max_length=100, choices=[('Tinto', 'Tinto'), ('Blanco', 'Blanco'), ('Rosado', 'Rosado')])
    anio_minimo = models.IntegerField(default=2000)
    anio_maximo = models.IntegerField(default=2023)
    
    def __str__(self):
        return f"Preferencias de {self.usuario.username}"

class Recomendacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendacion de {self.vino.nombre} para {self.usuario.username}"
