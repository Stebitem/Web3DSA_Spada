from django.contrib import admin
from .models import Categoria, Material, Pieza3D

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio_kg')

@admin.register(Pieza3D)
class Pieza3DAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','material','precio','fecha_creacion')
    list_filter = ('categoria','material')
    search_fields = ('nombre','descripcion')
