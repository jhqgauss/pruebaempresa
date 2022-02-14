from django.shortcuts import redirect, render
from .models import Modelo
# Create your views here.

def home(request):
    empresas=Modelo.objects.all()
    return render(request, "index.html", {"empresas": empresas}) 

def registrarempresa(request):
    nombre=request.POST['nombreempresa']
    nit=request.POST['nitempresa']
    direccion=request.POST['direempresa']
    telefono=request.POST['telempresa']

    empresa=Modelo.objects.create(nombre=nombre,nit=nit,direccion=direccion,telefono=telefono)
    return redirect('/')


def edicionempresa(request,nit):
    empresa=Modelo.objects.get(nit=nit)
    return (render(request, "edicionempresa.html",{"empresa":empresa}))


def editarempresa(request):
    nombre=request.POST['nombreempresa']
    nit=request.POST['nitempresa']
    direccion=request.POST['direempresa']
    telefono=request.POST['telempresa']

    empresa=Modelo.objects.get(nit=nit)
    empresa.nombre=nombre
    empresa.nit=nit
    empresa.direccion=direccion
    empresa.telefono=telefono
    empresa.save()
    return redirect('/')

def eliminarempresa(request,nit):
    empresa=Modelo.objects.get(nit=nit)
    empresa.delete()
    return redirect('/')