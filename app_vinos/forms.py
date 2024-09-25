from django import forms
from .models import Preferencia

class PreferenciaForm(forms.ModelForm):
    class Meta:
        model = Preferencia
        fields = ['tipo_vino', 'anio_minimo', 'anio_maximo']

class BuscarRecomendacionForm(forms.Form):
    tipo_vino = forms.ChoiceField(choices=[('Tinto', 'Tinto'), ('Blanco', 'Blanco'), ('Rosado', 'Rosado')])
    anio_minimo = forms.IntegerField()
    anio_maximo = forms.IntegerField()
