from django.forms import ModelForm
from django import forms
from .models import Sucursal, Usuario, Tipo_Usuario


from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model, password_validation

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'email']


class AdminFormaActualizar(forms.ModelForm):
    # variable para que el admin solo pueda ver la contraseña
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'password')

    def clean_password(self):
        return self.initial['password']

class AdminFormaCreacionUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        usuario = super(AdminFormaCreacionUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class UsuarioForm(forms.ModelForm):

    username = forms.CharField(initial='',help_text='')
    tipo_usuario = forms.ModelChoiceField(queryset=Tipo_Usuario.objects.all(), empty_label="Seleccione un tipo de usuario")
    password1 = forms.CharField(initial='', label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(initial='', label='Password confirmation', widget=forms.PasswordInput)

    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'tipo_usuario')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

#PRIMERO

# class UsuarioForm(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     username = forms.CharField(help_text='')
    
#     password1 = forms.CharField(
        
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        
#     )
#     password2 = forms.CharField(
        
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         strip=False,
        
#     )

#     class Meta:
#         model = Usuario
#         fields = ("username",'tipo_usuario')
        

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
#                 "autofocus"
#             ] = True

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError(
#                 self.error_messages["password_mismatch"],
#                 code="password_mismatch",
#             )
#         return password2

#     def _post_clean(self):
#         super()._post_clean()
#         # Validate the password after self.instance is updated with form data
#         # by super().
#         password = self.cleaned_data.get("password2")
#         if password:
#             try:
#                 password_validation.validate_password(password, self.instance)
#             except ValidationError as error:
#                 self.add_error("password2", error)

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
