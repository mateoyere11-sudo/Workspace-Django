from django import forms
from .models import Espacio, ServicioAdicional

class EspacioForm(forms.ModelForm):
    class Meta:
        model  = Espacio
        fields = '__all__'
        widgets = {
            'nombre_sala'        : forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_espacio'       : forms.Select(attrs={'class': 'form-control'}),
            'capacidad_personas' : forms.NumberInput(attrs={'class': 'form-control'}),
            'piso_edificio'      : forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_hora'        : forms.NumberInput(attrs={'class': 'form-control'}),
            'tiene_aire'         : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tiene_proyector'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'estado_disponible'  : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion'        : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ServicioAdicionalForm(forms.ModelForm):
    class Meta:
        model  = ServicioAdicional
        fields = '__all__'
        widgets = {
            'reserva'            : forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_servicio'      : forms.Select(attrs={'class': 'form-control'}),
            'descripcion'        : forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad'           : forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario'    : forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_total'        : forms.NumberInput(attrs={'class': 'form-control'}),
            'solicitud_especial' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hora_entrega'       : forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'estado_servicio'    : forms.Select(attrs={'class': 'form-control'}),
        }