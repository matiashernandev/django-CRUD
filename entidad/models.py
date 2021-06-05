from django.db import models

TIPO_DNI_CHOICE = {
    ("LC", "Libreta Civica"),
    ("LE", "Libreta Enrolamiento"),
    ("DU", "Documento Unico")
}

class Localidad(models.Model):
    nombre_l = models.CharField("Localidad", max_length=50)
    cp = models.CharField("Codigo Postal", max_length=20)
    provincia = models.CharField(max_length=50)
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return '%s - %s' % (self.cp, self.nombre_l)


class Persona(models.Model):
    # tipo_dni = models.CharField("Tipo de documento",choices=TIPO_DNI_CHOICE, max_length=5)
    # numero_doc = models.IntegerField("Nº de documento") #con migrate quizas 
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True) #null y blank para que no sea requeridos
    fecha_nac = models.DateField("Fecha de nacimiento")
    calle = models.CharField(max_length=100, null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE) #rever cascade
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)


class Categoria(models.Model):
    nombre = models.CharField(max_length=70, verbose_name='Categoría')
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Unidad_medida(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Unidad_medida')
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    codigo = models.CharField(max_length=150, null=True, unique=True, verbose_name='codigo', help_text='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre', help_text='Nombre')
    categoria = models.ForeignKey(Categoria, help_text='Categoría', on_delete=models.CASCADE)
    unidad_de_medida = models.ForeignKey(Unidad_medida, help_text='Unidad de medida', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True,
                                 help_text='PRECIO NETO')
    activo = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nombre)

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, null=True, blank=True)
    autonumerico = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.nombre


class Movimiento(models.Model):
    tipo = models.ForeignKey(TipoMovimiento, verbose_name="Tipo_movimiento", help_text="Tipo de movimiento", on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha", help_text="Fecha de carga")
    numero1 = models.CharField(max_length=5, default='00001', help_text="Número")
    numero = models.CharField(max_length=15)
    cliente = models.ForeignKey(Persona, limit_choices_to={'activo': True}, default='1',
                                help_text="Nº de documento o CUIT del Tercero", on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    articulo = models.ForeignKey(Articulo, related_name='Artículo', null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return '%s-%s %s' % (self.numero1, self.numero, self.tipo)

