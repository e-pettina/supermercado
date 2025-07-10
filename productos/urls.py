from django.urls import path
from .views import lista_productos, cargar_producto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('cargar/', cargar_producto, name='cargar_producto'),
]
