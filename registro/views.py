from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
import requests
import json




# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('inicioEmpleado')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    
def home(request):
    return render(request, 'home.html')

def tipoStock(request):
    return render(request, 'tipoStock.html')

def putDiario(request):
    
    if request.method == 'GET':
        url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/'
        response = requests.get(url)
        data = response.json()
        context = {'medicamentos': data}
        return render(request, 'stock_diario.html', context)
    elif request.method == 'POST':
        medicamento_id = request.POST.get('medicamento_id')
        print(medicamento_id)
        url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/{medicamento_id}/'
        new_stock = request.POST.get(f'stockDiario_{medicamento_id}')
        data = {'stockDiario': new_stock}
        response = requests.put(url, data=data)

        if response.status_code == 200:
            return redirect('http://127.0.0.1:8000/diarioSucursal/?sucursal=Sucursal 3')
        else:
            print(response.text)
            return render(request, 'inicioEmpleado.html')

def diario(request):

    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/'
    response = requests.get(url)
    data = response.json()
    context = {'medicamentos': data}
    return render(request, 'stock_diario.html', context)

def obtener_medicamentos(request):
    if request.method == 'POST':
        sucursal = request.POST.get('sucursal')
        url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/?sucursal={sucursal}'
        response = requests.get(url)
        data = json.loads(response.text)
        return render(request, 'stock_diario.html', {'medicamentos': data})

def diarioSucursal(request):
    if request.method == 'POST':
        sucursal = request.POST.get('sucursal')
        url = f'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/?sucursal={sucursal}'
        response = requests.get(url)
        data = json.loads(response.text)
        return render(request, 'stock_diario.html', {'medicamentos': data})

# def diarioSucursal(request):
#     url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/'
#     response = requests.get(url)
#     data = response.json()
#     context = {'medicamentos': data}
#     return render(request, 'stock_diario.html', context)
    

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
    pass

def update_stock(request):
    return redirect('diario')

def get_sucursales(request):
    url = 'https://vozparkinson.pythonanywhere.com/apis/medicamento_full/'
    response = requests.get(url)
    data = json.loads(response.text)
    sucursales = set()
    for item in data:
        sucursales.add(item['sucursal'])
    return render(request, 'sucursales.html', {'sucursales': sucursales})

# def my_view(request):
#     radio_value = request.POST.get('radioGroup')
#     if radio_value == "Diario":
#         return redirect('diario')
#     elif radio_value == "Semanal":
#         return redirect('semanal')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tipoStock')
        