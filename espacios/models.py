from django.db import models

class Espacio(models.Model):
    TIPO_CHOICES = [
        ('sala', 'Sala de Juntas'),
        ('escritorio', 'Escritorio Compartido'),
    ]

    nombre_sala        = models.CharField(max_length=100)
    tipo_espacio       = models.CharField(max_length=20, choices=TIPO_CHOICES)
    capacidad_personas = models.PositiveIntegerField()
    piso_edificio      = models.PositiveIntegerField()
    precio_hora        = models.DecimalField(max_digits=8, decimal_places=2)
    tiene_aire         = models.BooleanField(default=False)
    tiene_proyector    = models.BooleanField(default=False)
    estado_disponible  = models.BooleanField(default=True)
    descripcion        = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_sala

    class Meta:
        verbose_name        = "Espacio"
        verbose_name_plural = "Espacios"



#Servicio adicional


class ServicioAdicional(models.Model):
    TIPO_SERVICIO_CHOICES = [
        ('cafe', 'Café'),
        ('internet', 'Internet Dedicado'),
    ]
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    reserva            = models.IntegerField()
    tipo_servicio      = models.CharField(max_length=20, choices=TIPO_SERVICIO_CHOICES)
    descripcion        = models.CharField(max_length=200, blank=True)
    cantidad           = models.PositiveIntegerField(default=1)
    precio_unitario    = models.DecimalField(max_digits=8, decimal_places=2)
    costo_total        = models.DecimalField(max_digits=10, decimal_places=2)
    solicitud_especial = models.TextField(blank=True)
    hora_entrega       = models.TimeField(null=True, blank=True)
    estado_servicio    = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def save(self, *args, **kwargs):
        # Calcula el costo total automáticamente
        self.costo_total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_servicio} - Reserva #{self.reserva}"

    class Meta:
        verbose_name        = "Servicio Adicional"
        verbose_name_plural = "Servicios Adicionales"