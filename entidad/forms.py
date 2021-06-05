from django.forms import ModelForm, DateInput
from django import forms
from .models import Persona

class DateInput(forms.DateInput):
    input_type = "date"

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'edad': forms.TextInput(),
            'fecha_nac': DateInput(),
            'calle': forms.TextInput(),
            'localidad': forms.Select(),
            'email': forms.TextInput(),
            'activo': forms.CheckboxInput(),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
            
        }
