from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *

# Create your views here.
# comunidades = Comunidad.objects.all()
# delegadas = Delegada.objects.all()
# productos = Producto.objects.all()
# pedidos = Pedido.objects.all()

# context = {'comunidades': comunidades, 'delegadas': delegadas, 'productos': productos, 'pedidos': pedidos}

def home(request):
  return render(request, 'comunidades/home.html')

# # def comunidades(request):  
# #   return render(request, 'comunidades/comunidades.html', context)

# # def comunidad(request, pk):
# #   comunidad = Comunidad.objects.get(pk=pk)
# #   context_comunidad = {'comunidad': comunidad}
# #   return render(request, 'comunidades/comunidad.html', context_comunidad)

# def delegadas(request):
#   return render(request, 'comunidades/delegadas.html', context)

# def delegada(request, pk):
#   delegada = Delegada.objects.get(pk=pk)
#   context_delegada = {'delegada': delegada}
#   return render(request, 'comunidades/delegada.html', context_delegada)

# def productos(request):
#   return render(request, 'comunidades/productos.html', context)

# def producto(request, pk):
#   producto = Producto.objects.get(pk=pk)
#   context_producto = {'producto': producto}
#   return render(request, 'comunidades/producto.html', context_producto)

# def pedidos(request):
#   return render(request, 'comunidades/pedidos.html', context)

# def pedido(request, pk):
#   pedido = Pedido.objects.get(pk=pk)
#   context_pedido = {'producto': producto}
#   return render(request, 'comunidades/pedido.html', context_pedido)

class JSONResponse(HttpResponse):
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def comunidades_lista(request):
  if request.method == 'GET':
    comunidades = Comunidad.objects.all()
    serializer = ComunidadSerializer(comunidades, many=True)
    return JSONResponse(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ComunidadSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)

def comunidad_individual(request, pk):
  try:
    comunidad = Comunidad.objects.get(pk=pk)
  except Comunidad.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ComunidadSerializer(comunidad)
    return JSONResponse(serializer.data)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ComunidadSerializer(comunidad, data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    comunidad.delete()
    return HttpResponse(status=204)

@csrf_exempt
def delegadas_lista(request):
  if request.method == 'GET':
    delegadas = Delegada.objects.all()
    serializer = DelegadaSerializer(delegadas, many=True)
    return JSONResponse(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = DelegadaSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)

def delegada_individual(request, pk):
  try:
    delegada = Delegada.objects.get(pk=pk)
  except Delegada.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = DelegadaSerializer(delegada)
    return JSONResponse(serializer.data)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = DelegadaSerializer(delegada, data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    delegada.delete()
    return HttpResponse(status=204)

@csrf_exempt
def productos_lista(request):
  if request.method == 'GET':
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return JSONResponse(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ProductoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)

def producto_individual(request, pk):
  try:
    producto = Producto.objects.get(pk=pk)
  except Producto.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ProductoSerializer(producto)
    return JSONResponse(serializer.data)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ProductoSerializer(producto, data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    producto.delete()
    return HttpResponse(status=204)

@csrf_exempt
def pedidos_lista(request):
  if request.method == 'GET':
    pedidos = Pedido.objects.all()
    serializer = PedidoSerializer(pedidos, many=True)
    return JSONResponse(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = PedidoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)

def pedido_individual(request, pk):
  try:
    pedido = Pedido.objects.get(pk=pk)
  except Pedido.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = PedidoSerializer(pedido)
    return JSONResponse(serializer.data)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = PedidoSerializer(pedido, data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    pedido.delete()
    return HttpResponse(status=204)