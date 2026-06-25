from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'espacios', views.EspacioViewSet, basename='espacio-api')
router.register(r'servicios', views.ServicioAdicionalViewSet, basename='servicio-api')

urlpatterns = [
    # Espacio
    path('espacios/',                    views.espacio_lista,    name='espacio_lista'),
    path('espacios/nuevo/',              views.espacio_crear,    name='espacio_crear'),
    path('espacios/<int:pk>/editar/',    views.espacio_editar,   name='espacio_editar'),
    path('espacios/<int:pk>/eliminar/',  views.espacio_eliminar, name='espacio_eliminar'),
    # Servicio Adicional
    path('servicios/',                   views.servicio_lista,   name='servicio_lista'),
    path('servicios/nuevo/',             views.servicio_crear,   name='servicio_crear'),
    path('servicios/<int:pk>/editar/',   views.servicio_editar,  name='servicio_editar'),
    path('servicios/<int:pk>/eliminar/', views.servicio_eliminar,name='servicio_eliminar'),

    path('api/', include(router.urls))
]