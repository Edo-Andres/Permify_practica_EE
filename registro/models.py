from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(254)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.nombre
    
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