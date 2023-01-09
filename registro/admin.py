from django.contrib import admin
from .models import Empresa, Producto

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Empresa, EmpresaAdmin)

class ProductoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Producto, ProductoAdmin)
