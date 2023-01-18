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
      

def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "app/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
 
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
 
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
 
    contexto = {"profesores": profesores}
 
    return render(request, "app/leerProfesores.html", contexto)



def editarProfesor(request, profesor_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = Profesoresformulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "app/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = Profesoresformulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})

    # Voy al html que me permite editar
    return render(request, "app/editarprofesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

