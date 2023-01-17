from django.shortcuts import render
from django.http import HttpResponse
from mi_app.forms import *
from mi_app.models import *

# Create your views here.

def inicio(request):
    return render(request, 'app/inicio.html')


def curso(request):
    return render(request, 'app/curso.html')


def profesores(request):
    return render(request, 'app/profesores.html')


def estudiantes(request):
    return render(request, 'app/estudiantes.html')

def entregables(request):
    return render(request, 'app/entregables.html')



def curso(request):

      if request.method == "POST":

            miFormulario = Cursoformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "app/inicio.html")
      else:
            miFormulario = Cursoformulario()

      return render(request, "app/curso.html", {"miFormulario": miFormulario})





def profesores(request):

      if request.method == "POST":

            miFormulario = Profesoresformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion['email'], profesion=informacion['profesion'])
                  profesor.save()
                  return render(request, "app/inicio.html")
      else:
            miFormulario = Profesoresformulario()

      return render(request, "app/profesores.html", {"miFormulario": miFormulario})





def estudiantes(request):

      if request.method == "POST":

            miFormulario = Estudianteformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion['email'])
                  estudiante.save()
                  return render(request, "app/inicio.html")
      else:
            miFormulario = Estudianteformulario()

      return render(request, "app/estudiantes.html", {"miFormulario": miFormulario})





def entregables(request):

      if request.method == "POST":

            miFormulario = Entregablesformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  entrega = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion['entregado'])
                  entrega.save()
                  return render(request, "app/inicio.html")
      else:
            miFormulario = Entregablesformulario()

      return render(request, "app/entregables.html", {"miFormulario": miFormulario})


def busquedacamada(request):
      return render(request, 'app/busquedacamada.html')

def buscar(request):
      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "app/busquedacamada.html", {"cursos":cursos, "camada":camada})

      else: 
             respuesta = "No enviaste datos"
                        
      return HttpResponse(respuesta)
      