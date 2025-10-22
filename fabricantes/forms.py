from django import forms
from .models import Fabricante


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['Fabricante_id', 'Nombre', 'Pais', 'sitio_web', 'logo_url', 'email']
        labels = {
            'Fabricante_id': 'ID Fabricante',
            'Nombre': 'Nombre',
            'Pais': 'País',
            'sitio_web': 'Sitio Web',
            'logo_url': 'URL del Logo (Opciones: monitores.png, Tarjetas_Graficas.png, perifericos.png)',
            'email': 'Correo Electrónico'
        }
        widgets = {
            'Fabricante_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
            'logo_url': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
