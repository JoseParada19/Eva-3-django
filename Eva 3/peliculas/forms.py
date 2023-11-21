from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
            'fecha_estreno': forms.DateInput(attrs={'type': 'date'}),
            'duracion_pelicula': forms.TimeInput(attrs={'type': 'time'}),
        }
 
