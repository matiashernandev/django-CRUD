from django.urls import path
from . import views

#otras formas de importar views:
#from entidad import views
#import entidad.views as views



urlpatterns = [
    path("", views.index, name="index"),
    path("acerca", views.acerca_de, name='acerca'),
    path("cliente", views.cliente, name='cliente'),
    path("localidad", views.localidad, name='localidad'),
    path("nuevocliente", views.nuevo_cliente, name='nuevocliente'),
    path("editarcliente/(?P<pk>\d+)$", views.editar_cliente, name='editarcliente'),
    path("borrarcliente/(?P<pk>\d+)$", views.borrar_cliente, name='borrarcliente'),
]