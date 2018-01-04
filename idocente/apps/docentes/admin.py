from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from .models import Producto
from import_export import resources, admin as adminre

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(adminre.ImportExportModelAdmin):
    resource_class = ProductoResource
    list_display = ('id', 'nombre', 'precio', 'stock')
    list_editable = ('stock',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
