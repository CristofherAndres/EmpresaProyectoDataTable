from django import forms

class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()