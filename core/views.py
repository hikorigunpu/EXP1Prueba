from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
# Create your views here.

def home(request):
    lista = Vehiculo.objects.all()
    contexto = {
        'vehiculos': lista,
    }
    return render(request, 'core/index.html', contexto)

def form_vehiculo(request):
    contexto = { 
        'form': VehiculoForm(),
        }
    if request.method=='POST':
        formulario=VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form-vehiculo.html', contexto)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    contexto = { 
        'form': VehiculoForm(instance=vehiculo),
        }
    if request.method=='POST':
        formulario=VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos modificados correctamente'
    return render(request, 'core/form-mod-vehiculo.html', contexto)

def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="home")

def login(request):
    return render(request, 'core/login.html')

def index2(request):
    return render(request, 'core/index2.html')

def loginnewuser(request):
    return render(request, 'core/loginnewuser.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')

def form(request):
    return render(request, 'core/form.html')

def obrasform(request):
    return render(request, 'core/obrasForm.html')

def profile(request):
    return render(request, 'core/profile.html')

def galery1(request):
    return render(request, 'core/galery1.html')

def galery2(request):
    return render(request, 'core/galery2.html')

def galery3(request):
    return render(request, 'core/galery3.html')



def galery1alt(request):
    return render(request, 'core/alt/galery1-notlog.html')

def galery2alt(request):
    return render(request, 'core/alt/galery2-notlog.html')

def galery3alt(request):
    return render(request, 'core/alt/galery3-notlog.html')

def aboutusalt(request):
    return render(request, 'core/alt/aboutus-notlog.html')

def formalt(request):
    return render(request, 'core/alt/form-notlog.html')

