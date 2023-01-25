from django.contrib import admin

from registro.forms import AdminFormaActualizar, AdminFormaCreacionUsuario
from .models import  Producto, Usuario, Tipo_Usuario

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

# class EmpresaAdmin(admin.ModelAdmin):
#   readonly_fields = ('created', )

# admin.site.register(Empresa, EmpresaAdmin)

class ProductoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Producto, ProductoAdmin)


  


class Tipo_UsuarioAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )
admin.site.register(Tipo_Usuario, Tipo_UsuarioAdmin)





class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

class UserAdmin(BaseUserAdmin):
    
    form = AdminFormaActualizar
    add_form = AdminFormaCreacionUsuario


    #list_display = ('email', 'username')
    list_filter = ('username',)
    fieldsets = (
        (None,{'fields': ('username','email', 'password')}),
        ('Informacion personal', {'fields': ( 'first_name', 'last_name', 'tipo_usuario')}),
        ('Permisos Django', {'fields': ('is_staff', 'is_active', 'groups')})

    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('username','password1', 'password2')
        }),
    )

    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(Usuario, UserAdmin )