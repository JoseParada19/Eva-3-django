from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

