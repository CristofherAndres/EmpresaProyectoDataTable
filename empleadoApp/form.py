from django import forms
from empleadoApp.models import Empleado
#Importar libreria para validar datos
from wsgiref.validate import validator
from django.core import validators

# Para editar 
class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField(validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(10)
        ]
    )
    email = forms.CharField(max_length=50)
    telefono = forms.CharField(required=False)

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("El correo debe contener un @")
        return inputEmail

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'

    nombre.label = "Nombre Empleado"
    email.label = "Email Empleado"
    telefono.label = "Telefono Empleado"

# Se llama para guardar los datos
class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    #Validaciones estandar
    nombre = forms.CharField(validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(10)
        ]
    )
    email = forms.CharField(max_length=50)
    telefono = forms.CharField(required=False) # Opcional
     
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("El correo debe contener un @")
        return inputEmail

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'

    nombre.label = "Nombre"
    email.label = "Email"
    telefono.label = "Telefono"