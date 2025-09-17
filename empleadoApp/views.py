from django.shortcuts import render
from empleadoApp.models import Empleado

# Create your views here.

def empleadoData(request):
    #importar datos de la DB con el ORM (SELECT * FROM XX;)
    empleados = Empleado.objects.all()
    data = {'empleados':empleados}
    return render (request, 'empleadoApp/empleados.html', data)