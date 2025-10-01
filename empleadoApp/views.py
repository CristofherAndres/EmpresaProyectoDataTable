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
    form = EmpleadoRegistroForm() # Crea un formulario en blanco
    
    # Solo se ejecuta cuando se apreta enviar datos
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('empleadosData'))                  

    data = {'form' : form,
            'titulo' : 'Crear empleado',
            'txtBoton' : 'Guardar empleado'}
    return render(request, 'empleadoApp/empleadoRegistro.html' ,data)

def editarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id) # Obtengo los datos del empleado que quiero editar
    form = EmpleadoRegistroForm(instance=empleado) # Formulario cargaria los datos del empleado
    
    # Solo se ejecuta cuando se apreta enviar datos
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST, instance=empleado) # Editan los datos del empleado actual
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('empleadosData'))                  

    data = {'form' : form,
            'titulo' : 'Editar empleado',
            'txtBoton' : 'Guardar cambios'}
    return render(request, 'empleadoApp/empleadoRegistro.html' ,data)

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return HttpResponseRedirect(reverse('empleadosData'))  