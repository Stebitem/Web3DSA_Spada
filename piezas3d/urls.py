from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('piezas/', views.listar_piezas, name='listar_piezas'),
    path('piezas/nuevo/', views.crear_pieza, name='crear_pieza'),
    path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
    path('material/nuevo/', views.crear_material, name='crear_material'),
]
