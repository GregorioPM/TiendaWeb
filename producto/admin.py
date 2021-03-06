from django.contrib import admin
from .models import producto
from .models import categoria
from .models import marca
from .models import empresa
# Register your models here.

class listarProducto(admin.ModelAdmin):
    list_display= [
        "idCurso", "referencia", "nombre","valor","estado", "categoria","marca"
    ]

admin.site.register(producto, listarProducto)

admin.site.register(marca)

admin.site.register(categoria)

admin.site.register(empresa)

admin.site.site_header="Administrador DevSystem"