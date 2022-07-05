from django.shortcuts import render, redirect
from .models import obra
from .forms import obraform, userform
from django.views.generic import CreateView
# Create your views here.

def listadouser(request):
    lista = obra.objects.all()
    contexto = {
        'obra': lista,
    }
    return render(request, 'core/listadouser.html', contexto)

def form_obra(request):
    contexto = { 
        'form': obraform(),
        }
    if request.method=='POST':
        formulario=obraform(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form-obra.html', contexto)


class ObraCreateView(CreateView):
    model = obra
    fields = ['idobra','autor','nombre','descripcion','nombretecnica','precio','imagen']

def form_mod_obra(request, id):
    obra1 = obra.objects.get(idobra=id)
    contexto = { 
        'form': obraform(instance=obra1),
        }
    if request.method=='POST':
        formulario=obraform(data=request.POST, instance=obra1)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos modificados correctamente'
    return render(request, 'core/form-mod-obra.html', contexto)

def form_del_obra(request, id):
    obra1 = obra.objects.get(idobra=id)
    obra1.delete()
    return redirect(to="listadouser")

def login(request):
    return render(request, 'core/login.html')
def filtro(request):
    return render(request, 'core/filtro.html')

def css1(request):
    return render(request, 'core/css/stylesheet.css')

def index2(request):
    lista = obra.objects.all()
    contexto = {
        'obra': lista,
    }
    return render(request, 'core/index2.html', contexto)
def index(request):
    lista = obra.objects.all()
    contexto = {
        'obra': lista,
    }
    return render(request, 'core/index.html', contexto)

def home(request):
    return render(request, 'core/index.html')

def loginnewuser(request):
    contexto = { 
        'form': userform(),
        }
    if request.method=='POST':
        formulario=userform(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/loginnewuser.html', contexto)

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

def galerymod(request, nombre):
    lista = obra.objects.get(nombre=nombre)
    contexto = {
        'obra': lista,
    }
    return render(request, 'core/galerymod.html', contexto)

def allobras(request):
    return render(request, 'core/allobras.html')

def allobrasalt(request):
    return render(request, 'core/allobrasalt.html')

