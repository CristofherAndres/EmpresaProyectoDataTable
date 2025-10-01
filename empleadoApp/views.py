from django.shortcuts import render
from empleadoApp.models import Empleado
from empleadoApp.form import EmpleadoRegistroForm

# Redirigir a al sitio deseado
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def empleadoData(request):
    #importar datos de la DB con el ORM (SELECT * FROM XX;)
    empleados = Empleado.objects.all()
    data = {'empleados':empleados}
    return render (request, 'empleadoApp/empleados.html', data)

def crearEmpleado(request):
    form = EmpleadoRegistroForm()
    
    # Solo se ejecuta cuando se apreta enviar datos
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('empleadosData'))                  

    data = {'form' : form}
    return render(request, 'empleadoApp/empleadoRegistro.html' ,data)