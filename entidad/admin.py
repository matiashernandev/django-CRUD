from django.contrib import admin

# Register your models here.
from entidad import models


my_models = [models.Persona, models.Localidad, models.Categoria, models.Articulo, models.Movimiento]

admin.site.register(my_models)