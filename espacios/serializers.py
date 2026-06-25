from rest_framework import serializers
from .models import Espacio, ServicioAdicional

class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'

class ServicioAdicionalSerializer(serializers.ModelSerializer):
    costo_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # ← añade esto
    class Meta:
        model = ServicioAdicional
        fields = '__all__'