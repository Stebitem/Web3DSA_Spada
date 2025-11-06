from django import forms
from .models import Categoria, Material, Pieza3D

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre','descripcion','precio_kg']

class Pieza3DForm(forms.ModelForm):
    class Meta:
        model = Pieza3D
        fields = ['nombre','descripcion','categoria','material','precio','imagen']
