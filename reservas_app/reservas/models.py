from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio_noche = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='habitaciones/', blank=True, null=True)


    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField(default=timezone.now)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    comprobante = models.ImageField(upload_to='comprobantes/', null=True, blank=True)

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} ({self.habitacion.numero})"