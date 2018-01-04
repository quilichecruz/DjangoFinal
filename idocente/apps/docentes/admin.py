from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from .models import Categoria, Insumo, Producto
from import_export import resources, admin as adminre

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(adminre.ImportExportModelAdmin):
    resource_class = ProductoResource
    list_display = ('id','imagen_recortada', 'nombre', 'categoria', 'precio', 'stock')
    list_editable = ('stock',)
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    filter_horizontal = ('insumo', )

    def imagen_recortada(self, obj):
        try:
            if obj.imagen is None or obj.imagen is '':
                return ''
            else:
                im = get_thumbnail(obj.imagen, '80x80', crop='center', quality=99)
                html = '<image src="%s" width="80" height="80">' % (im.url)
                return html
        except:
            return ''

    imagen_recortada.short_description = 'Imagen'
    imagen_recortada.allow_tags = True