from rest_framework import serializers
from .models import *

class ComunidadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comunidad
    fields = ('id', 'nombre', 'productos')
  
class DelegadaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Delegada  
    fields = ('id', 'nombre', 'comunidad')

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = ('id', 'nombre', 'descripción', 'alto', 'ancho', 'profundidad', 'diámetro', 'color', 'tejido', 'imagen')

class PedidoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pedido
    fields = ('id', 'producto', 'fecha_creación', 'estado', 'cantidad')
  