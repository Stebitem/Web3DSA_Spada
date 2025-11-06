# Web3DSA_Spada

Proyecto Django para la consigna: gestión de piezas impresas en 3D.

## Requisitos de la consigna cubiertos
- Herencia de templates (base.html)
- Modelos: Categoria, Material, Pieza3D
- Formularios para las 3 clases
- Vista con listado de objetos (piezas)
- Barra de búsqueda en el listado
- README con orden de pruebas
- .gitignore, requirements.txt

## Cómo probar
1. Crear y activar virtualenv:
   python -m venv .venv
   .venv\Scripts\activate
2. Instalar dependencias:
   pip install -r requirements.txt
3. Migrar y crear superuser si querés:
   python manage.py migrate
   python manage.py createsuperuser
4. Ejecutar servidor:
   python manage.py runserver
5. Abrir: http://127.0.0.1:8000/

## Rutas principales
- / -> inicio
- /piezas/ -> listado y búsqueda
- /piezas/nuevo/ -> crear pieza
- /categoria/nuevo/ -> crear categoría
- /material/nuevo/ -> crear material

