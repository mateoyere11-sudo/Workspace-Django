from django.db import models

class Cliente(models.Model):
    razon_social = models.CharField(max_length=100)
    identificacion_fiscal = models.CharField(max_length=50)
    nombre_representante = models.CharField(max_length=100)
    correo_corporativo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion_facturacion = models.CharField(max_length=150)
    tipo_cliente = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    historial_reportes = models.TextField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.razon_social