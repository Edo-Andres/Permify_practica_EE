from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
import requests
import json
from django.urls import reverse
from datetime import datetime as date
import datetime

from registro.models import Usuario, Tipo_Usuario
from .forms import UsuarioForm

from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages







# Create your views here.

def is_gerente(user:Usuario):
    if user.is_authenticated:
        if user.tipo_usuario:
            return user.tipo_usuario.nombre_tipo_usuario == 'Gerente'
    return False

@user_passes_test(is_gerente, login_url='signin')
# def signup(request):
    
#     data = {
#         'form': UsuarioForm(),
        
#     }

#     if request.method == 'POST':
#         formulario = UsuarioForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             # resibir usuario y password para hacer un login automatico
#             user = authenticate(
#                 username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
#             # login(request, user)
#             # message.success(request, 'Te has registrado correctamente')
#             return redirect(to='signin')
#         data["form"] = formulario

#     return render(request, 'signup.html', data)

    # INTENTO

def signup(request):
    
    data = {
        'form': UsuarioForm(),
        
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # resibir usuario y password para hacer un login automatico
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            # login(request, user)
            # message.success(request, 'Te has registrado correctamente')
            return redirect(to='signin')
        else:
            if 'password2' in formulario.errors:
                messages.error(request, 'Passwords no coinciden')
        data["form"] = formulario
    return render(request, 'signup.html', data)


    


    # PRIMERO
    # if request.method == 'GET':
    #     return render(request, 'signup.html', {"form":UsuarioForm})
    # else:
    #     if request.POST["password1"] == request.POST["password2"]:
    #         try:
    #             user = Usuario.objects.create_user(request.POST["username"], password=request.POST["password1"], tipo_usuario= request.POST["tipo_usuario"])
    #             user.set_password(request.POST["password1"])
    #             user.save()
    #             login(request, user)
    #             return redirect('inicioEmpleado')
    #         except IntegrityError:
    #             return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        # return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    
def home(request):
    return render(request, 'home.html')

def tipoStock(request):
    return render(request, 'tipoStock.html')

def tipoReporte(request):
    return render(request, 'tipoReporte.html')


def putDiario(request):
    array_stock = []
    for stock in request.POST.get('stockDiario'):
        print(stock)
 
    # username = 'admin_medicamento'
    # password ='admin'
    # if request.method == 'POST':
    #     medicamento_id = request.POST.get('medicamento_id')
    #     sucursal = request.POST.get('sucursal')
    #     fecha_actu_stock = request.POST.get('fecha_actu_stock')
    #     print(medicamento_id)   
    #     print(sucursal)
    #     print(fecha_actu_stock)
    #     url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full{medicamento_id}/'
    #     new_stock = request.POST.get(f'stockDiario_{medicamento_id}')
    #     now = date.now()
    #     new_fecha = now.strftime("%Y-%m-%d %H:%M:%S")
    #     data = {'stockDiario': new_stock, 'fecha_actu_stock': new_fecha}
        
    #     response = requests.put(url, data=data,auth=(username,password))
    #     if response.status_code == 200:
    #         url2 = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}'
    #         response2 = requests.get(url2,auth=(username,password))
    #         data2 = json.loads(response2.text)
    #         return render(request, 'stock_diario.html', {'medicamentos': data2, 'sucursal':sucursal})
    #     else:
    #         print(response.text)
    #         return render(request, 'home.html')




def obtener_medicamentos(request):
    if request.method == 'POST':
        sucursal = request.POST.get('sucursal')
        url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}'
        response = requests.get(url)
        data = json.loads(response.text)
        return render(request, 'stock_diario.html', {'medicamentos': data})

def diarioSucursal(request):
    username = 'admin_medicamento'
    password ='admin'
    if request.method == 'POST':
        sucursal = request.POST.get('sucursal')
        url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}'
        response = requests.get(url,auth=(username,password))
        data = json.loads(response.text)
        return render(request, 'stock_diario.html', {'medicamentos': data, 'sucursal':sucursal, 'user':request.user})

def semanalSucursal(request):
    username = 'admin_medicamento'
    password ='admin'
    if request.method == 'POST':
        sucursal = request.POST.get('sucursal')
        url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}'
        response = requests.get(url,auth=(username,password))
        data = json.loads(response.text)
        return render(request, 'stock_semanal.html', {'medicamentos': data, 'sucursal':sucursal, 'user':request.user})
    
# def diarioSucursal(request):
#     url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
#     response = requests.get(url)
#     data = response.json()
#     context = {'medicamentos': data}
#     return render(request, 'stock_diario.html', context)

def diario(request):

    username = 'admin_medicamento'
    password ='admin'
    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
    response = requests.get(url,auth=(username,password))
    data = response.json()
    context = {'medicamentos': data}
    return render(request, 'stock_diario.html', context) 

def semanal(request):
    return render(request, 'stock_semanal.html')

def inicioEmpleado(request):
    if request.method == 'GET':
        return render(request, 'inicioEmpleado.html')
    else:
        radio_value = request.POST('radioGroup')
        if radio_value == "Diario":
            return redirect('diario')
        elif radio_value == "Semanal":
            return redirect('semanal')

def inicioGerente(request):
    return render(request, 'inicioGerente.html')

def update_stock(request):
    return redirect('diario')

# def get_reporte_diario(request):
#     username = 'admin_medicamento'
#     password ='admin'
#     url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
#     response = requests.get(url,auth=(username,password))
#     data = json.loads(response.text)
#     sucursales = set()
#     for item in data:
#         sucursales.add(item['sucursal'])

#     return render(request, 'reporteDiario.html', {'sucursales': sucursales})


def get_reporte_diario(request):
    username = 'admin_medicamento'
    password ='admin'
    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
    response = requests.get(url,auth=(username,password))
    data = json.loads(response.text)
    sucursales = set()
    for item in data:
        sucursales.add(item['sucursal'])
    sucursales_data = []
    for sucursal in sucursales:
        estado = 'Ok'
        for item in data:
            if item['sucursal'] == sucursal:
                fecha_actu_stock = datetime.datetime.strptime(item['fecha_actu_stock'], '%Y-%m-%dT%H:%M:%S-03:00')
                if fecha_actu_stock.date() != datetime.datetime.now().date():
                    estado = 'Pendiente'
                    break
        sucursales_data.append({'sucursal': sucursal, 'estado': estado})
    return render (request, 'reporteDiario.html',  {'sucursales_data': sucursales_data})


def get_reporte_semanal(request):
    username = 'admin_medicamento'
    password ='admin'
    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
    response = requests.get(url,auth=(username,password))
    data = json.loads(response.text)
    sucursales = set()
    for item in data:
        sucursales.add(item['sucursal'])
    sucursales_data = []
    for sucursal in sucursales:
        estado = 'Ok'
        for item in data:
            if item['sucursal'] == sucursal:
                fecha_actu_stock = datetime.datetime.strptime(item['fecha_actu_stock'], '%Y-%m-%dT%H:%M:%S-03:00')
                if fecha_actu_stock.date() != datetime.datetime.now().date():
                    estado = 'Pendiente'
                    break
        sucursales_data.append({'sucursal': sucursal, 'estado': estado})
    return render (request, 'reporteSemanal.html',  {'sucursales_data': sucursales_data})




def get_sucursales(request):
    username = 'admin_medicamento'
    password ='admin'
    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
    response = requests.get(url,auth=(username,password))
    data = json.loads(response.text)
    sucursales = set()
    for item in data:
        sucursales.add(item['sucursal'])
    
    if request.method == "POST":
        sucursal = request.POST.get("sucursal")
                
        return redirect("put_registros", sucursal)   
    return render(request, 'sucursales.html', {'sucursales': sucursales})

#Buena
# def get_sucursales(request):
#     username = 'admin_medicamento'
#     password ='admin'
#     url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
#     response = requests.get(url,auth=(username,password))
#     data = json.loads(response.text)
#     sucursales = set()
#     for item in data:
#         sucursales.add(item['sucursal'])
#     if request.method == "POST":
#         sucursal = request.POST.get("sucursal") 
        
#         return redirect("put_registros", sucursal)   
#     return render(request, 'sucursales.html', {'sucursales': sucursales})

def get_sucursales_semanal(request):
    username = 'admin_medicamento'
    password ='admin'
    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full'
    response = requests.get(url,auth=(username,password))
    data = json.loads(response.text)
    sucursales = set()
    for item in data:
        sucursales.add(item['sucursal'])
    return render(request, 'sucursales_semanal.html', {'sucursales': sucursales})
# def my_view(request):
#     radio_value = request.POST.get('radioGroup')
#     if radio_value == "Diario":
#         return redirect('diario')
#     elif radio_value == "Semanal":
#         return redirect('semanal')

# def signin(request):
#     if request.method == 'GET':
#         return render(request, 'signin.html', {"form": AuthenticationForm})
#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

#         login(request, user)
#         return redirect('tipoStock')
        

def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user:Usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        
        if user is not None:
            login(request, user)
            if user.tipo_usuario.nombre_tipo_usuario == 'Empleado':
                return redirect('tipoStock')
            if user.tipo_usuario.nombre_tipo_usuario == 'Gerente':
                return redirect('tipoReporte')
                            
        else:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})


def put_registros(request, sucursal):

    url = f"https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}&frecuencia_stock=d"
    print(url)
    
    username = "admin"
    password = "admin"
    response = requests.get(url,auth=(username,password))
    json_response = json.loads(response.text)

    data = {
        "json_response" : json_response
    }
    array_stocks = []
    if request.method == 'POST':
        url = f"https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}&frecuencia_stock=d"
        
        #mostrar todos los elementos del request
        for key, value in request.POST.items():
            #print('Key: %s' % (key) ) 
            #print('Value %s' % (value) )
            #agrego al array los valores
            array_stocks.append(value)
        #elimino el primer valor del array por que el tocken del formulario
       
        array_stocks.pop(0)
        now = date.now()
        new_fecha = now.strftime("%Y-%m-%d %H:%M:%S")
        response = requests.put(url, json={"stockDiario": array_stocks, "fecha_actu_stock":new_fecha}, auth = (username, password))
        
        return redirect(to ="sucursales")
        #return redirect('tipoReporte')
    return render(request, 'put_registros.html', {'json_response': json_response, 'sucursal': sucursal})


def put_registros_semanal(request, sucursal):

    url = f"https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}"
    print(url)
    
    username = "admin"
    password = "admin"
    response = requests.get(url,auth=(username,password))
    json_response = json.loads(response.text)

    data = {
        "json_response" : json_response
    }
    array_stocks = []
    if request.method == 'POST':
        print('#################################################################################')
        url = f"https://vozparkinson.pythonanywhere.com/apis/medicamento_full?sucursal={sucursal}"
        
        #mostrar todos los elementos del request
        for key, value in request.POST.items():
            #print('Key: %s' % (key) ) 
            #print('Value %s' % (value) )
            #agrego al array los valores
            array_stocks.append(value)
        #elimino el primer valor del array por que el tocken del formulario
       
        array_stocks.pop(0)
        
        print(array_stocks)
        now = date.now()
        new_fecha = now.strftime("%Y-%m-%d %H:%M:%S")
        response = requests.put(url, json={"stockDiario": array_stocks, "fecha_actu_stock":new_fecha}, auth = (username, password))
        
        return redirect(to ="sucursales_semanal")
        #return redirect('tipoReporte')
    return render(request, 'put_registros_semanal.html', {'json_response': json_response, 'sucursal': sucursal})
