import os
import django

# Establece el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings.base')
django.setup()

from apps.blog.models import Categoria

# Función para agregar nuevas categorías
def agregar_categorias(nombres_categorias):
    for nombre in nombres_categorias:
        categoria, created = Categoria.objects.get_or_create(nombre=nombre)
        if created:
            print(f'Categoría "{nombre}" creada correctamente.')
        else:
            print(f'La categoría "{nombre}" ya existe.')

# Lista de nombres de nuevas categorías
nuevas_categorias = [
    'Amenazas Cibernéticas',
    'Seguridad en Redes',
    'Privacidad en Línea',
    'Cumplimiento y Normativas',
    'Tecnologías Emergentes en Ciberseguridad',
]

# Llamar a la función para agregar las nuevas categorías
if __name__ == '__main__':
    agregar_categorias(nuevas_categorias)