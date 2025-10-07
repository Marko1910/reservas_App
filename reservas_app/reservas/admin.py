from django.contrib import admin
from .models import Cliente, Habitacion, Reserva

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'precio_noche', 'disponible')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'habitacion', 'fecha_inicio', 'fecha_fin', 'fecha_reserva')
