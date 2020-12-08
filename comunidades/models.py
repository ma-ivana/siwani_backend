from django.db import models

# Create your models here.
class Delegada(models.Model):
  nombre = models.CharField(max_length=300, null=True)
  comunidad = models.ForeignKey('Comunidad', null=True, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.nombre}, comunidad: {self.comunidad}"

class Producto(models.Model):
  nombre = models.CharField(max_length=100, null=True)
  descripción = models.CharField(max_length=1000, null=True)
  alto = models.DecimalField(null=True, max_digits=20, decimal_places=2, default=0.00)
  ancho = models.DecimalField(null=True, max_digits=20, decimal_places=2, default=0.00)
  profundidad = models.DecimalField(null=True, max_digits=20, decimal_places=2, default=0.00)
  diámetro = models.DecimalField(null=True, max_digits=20, decimal_places=2, default=0.00)
  color = models.CharField(max_length=100, null=True)
  tejido = models.CharField(max_length=100, null=True)
  imagen = models.ImageField(upload_to='comunidades')

  def __str__(self):
    return self.nombre
  

#check instructions in https://docs.djangoproject.com/en/3.1/topics/files/ in Using files in models

class Comunidad(models.Model):
  nombre = models.CharField(max_length=300, null=True)
  productos = models.ManyToManyField(Producto)

  def __str__(self):
    return self.nombre

class Pedido(models.Model):
  ESTADO = (
            ('Pendiente', 'Pendiente'),
            ('Solicitado', 'Solicitado'),
            ('Confirmado', 'Confirmado'),
            ('Finalizado', 'Finalizado')
            )
  producto = models.ForeignKey('Producto', null=True, on_delete=models.CASCADE)
  fecha_creación =  models.DateTimeField(auto_now_add=True, null=True)
  estado = models.CharField(max_length=20, null=True, choices=ESTADO)
  cantidad = models.PositiveIntegerField(default=1)
  delegada = models.ForeignKey('Delegada', null=True, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.producto}, cantidad: {self.cantidad}, delegada: {self.delegada}"