from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Modelo para Tipo_Usuario
class Tipo_Usuario(models.Model):
    id_tipo_usuario=models.AutoField('id tipo usuario',primary_key=True)
    nombre_tipo_usuario = models.CharField('Nombre tipo usuario', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre_tipo_usuario

class Usuario(AbstractUser):
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE, verbose_name="Tipo Usuario", null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  self.username
        
    class Meta:
        ordering = ['username']

# class Empresa(models.Model):
#     nombre = models.CharField(max_length=200)
#     direccion = models.TextField(max_length=250)
#     created = models.DateTimeField(auto_now_add=True)
#     email = models.EmailField(254)
#     user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

#     def __str__(self):
#         return self.nombre
    
class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(254)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    sku = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f' {self.sku}  {self.nombre} '