from django.forms import ModelForm
from .models import Sucursal

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'email']