from django.shortcuts import render
from empleadoApp.models import Empleado
from empleadoApp.form import EmpleadoRegistroForm

# Create your views here.

def empleadoData(request):
    #importar datos de la DB con el ORM (SELECT * FROM XX;)
    empleados = Empleado.objects.all()
    data = {'empleados':empleados}
    return render (request, 'empleadoApp/empleados.html', data)

def crearEmpleado(request):
    form = EmpleadoRegistroForm()
    data = {'form' : form}
    return render(request, 'empleadoApp/empleadoRegistro.html' ,data)