from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razón social'}),
            'identificacion_fiscal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUC / NIT / RFC'}),
            'nombre_representante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'correo_corporativo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@empresa.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+00 000 000 0000'}),
            'direccion_facturacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección completa'}),
            'tipo_cliente': forms.Select(
                attrs={'class': 'form-select'},
                choices=[
                    ('', 'Selecciona un tipo'),
                    ('empresa', 'Empresa'),
                    ('particular', 'Particular'),
                    ('gobierno', 'Gobierno'),
                ]
            ),
            'fecha_registro': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'historial_reportes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones o historial...'}),
            'estado': forms.Select(
                attrs={'class': 'form-select'},
                choices=[
                    ('', 'Selecciona un estado'),
                    ('activo', 'Activo'),
                    ('inactivo', 'Inactivo'),
                    ('suspendido', 'Suspendido'),
                ]
            ),
        }
        labels = {
            'razon_social': 'Razón Social',
            'identificacion_fiscal': 'Identificación Fiscal',
            'nombre_representante': 'Nombre del Representante',
            'correo_corporativo': 'Correo Corporativo',
            'telefono': 'Teléfono',
            'direccion_facturacion': 'Dirección de Facturación',
            'tipo_cliente': 'Tipo de Cliente',
            'fecha_registro': 'Fecha de Registro',
            'historial_reportes': 'Historial / Reportes',
            'estado': 'Estado',
        }