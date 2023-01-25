"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('inicioEmpleado/', views.inicioEmpleado, name='inicioEmpleado'),
    path('inicioGerente/', views.inicioGerente, name='inicioGerente'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('diario/', views.diario, name='diario'),
    path('semanal/', views.semanal, name='semanal'),
    path('update_stock/', views.update_stock, name='update_stock'),
    path('putDiario/', views.putDiario, name='putDiario'),
    path('sucursales/', views.get_sucursales, name='sucursales'),
    path('sucursales_semanal/', views.get_sucursales_semanal, name='sucursales_semanal'),
    path('tipoStock/', views.tipoStock, name='tipoStock'),
    path('diarioSucursal/', views.diarioSucursal, name='diarioSucursal'),    
    path('semanalSucursal/', views.semanalSucursal, name='semanalSucursal'),
    path('signout/', views.signout, name='signout'),

]
