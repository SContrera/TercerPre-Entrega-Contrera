from django import forms


class Cursoformulario(forms.Form):

    nombre=forms.CharField(max_length=40)
    camada = forms.IntegerField()

    def __str__(self) :
        return f' Nombre: {self.nombre} - Camada: {self.camada} '


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