from django import forms


class Cursoformulario(forms.Form):

    nombre=forms.CharField()
    camada = forms.IntegerField()

    # def __str__(self) :
    
    #     return f' nombre: {self.nombre} - Camada: {self.camada} '


class Estudianteformulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class Profesoresformulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class Entregablesformulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()  
    entregado = forms.BooleanField()


#importaciones necesarias para login mejorado.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}