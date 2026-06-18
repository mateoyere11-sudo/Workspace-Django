from django.urls import path
from . import views

urlpatterns=[

path('',views.lista_clientes,name='lista'),

path('nuevo/',views.crear_cliente,name='nuevo'),

path('editar/<int:id>/',views.editar_cliente,name='editar'),

path('eliminar/<int:id>/',views.eliminar_cliente,name='eliminar'),

]