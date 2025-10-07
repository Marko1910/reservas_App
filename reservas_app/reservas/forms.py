from django import forms
from .models import Cliente, Reserva

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        # Se agregan los campos reales de una reserva sin quitar lo que ya tenías
        fields = ['cliente', 'habitacion', 'fecha_inicio', 'fecha_fin', 'comprobante']

        # Opcional, pero mejora el formulario visualmente
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'habitacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Habitación Doble'}),
            'fecha_inicio': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'fecha_fin': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'comprobante': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }