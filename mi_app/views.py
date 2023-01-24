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




def leerCursos(request):

      cursos = Curso.objects.all() #trae todos los profesores

      contexto= {"cursos":cursos} 

      return render(request, "app/leercursos.html",contexto)


def eliminarCurso(request, curso_nombre):

      
      curso = Curso.objects.get(nombre=curso_nombre)
      
      curso.delete()
 
    # vuelvo al menú
      cursos = Curso.objects.all()  # trae todos los profesores
 
      contexto = {"cursos": cursos}
 
      return render(request, "app/leercursos.html", contexto)

def editarCurso(request, curso_nombre):
      
       curso = Curso.objects.get(nombre=curso_nombre)

       # Si es metodo POST hago lo mismo que el agregar
       if request.method == 'POST':
            
            miFormulario = Cursoformulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:
                  
                  
                  informacion = miFormulario.cleaned_data

                  curso.nombre = informacion['nombre']
                  curso.camada = informacion['camada']

                  curso.save()
            # Vuelvo al inicio o a donde quieran
                  return render(request, "app/inicio.html")
            
            
            
             # En caso que no sea post
       else:

            miFormulario = Cursoformulario(initial={'nombre': curso.nombre, 'camada': curso.camada})

        # Voy al html que me permite editar
            return render(request, "app/editarcurso.html", {"miFormulario": miFormulario, "curso_nombre": curso_nombre})


def leerEstudiantes(request):

      estudiantes = Estudiante.objects.all() #trae todos los profesores

      contexto= {"estudiantes":estudiantes} 

      return render(request, "app/leerestudiantes.html",contexto)


def eliminarEstudiantes(request, estudiante_nombre):

      
      estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
      
      estudiante.delete()
 
    # vuelvo al menú
      estudiantes = Estudiante.objects.all()  # trae todos los profesores
 
      contexto = {"estudiantes": estudiantes}
 
      return render(request, "app/leerestudiantes.html", contexto)



def editarEstudiante(request, estudiante_nombre):
      
       estudiante = Estudiante.objects.get(nombre=estudiante_nombre)

       # Si es metodo POST hago lo mismo que el agregar
       if request.method == 'POST':
            
            miFormulario = Estudianteformulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:
                  
                  
                  informacion = miFormulario.cleaned_data

                  estudiante.nombre = informacion['nombre']
                  estudiante.apellido = informacion['apellido']

                  estudiante.save()
            # Vuelvo al inicio o a donde quieran
                  return render(request, "app/inicio.html")
            
            
            
             # En caso que no sea post
       else:

            miFormulario = Estudianteformulario(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido})

        # Voy al html que me permite editar
            return render(request, "app/editarestudiante.html", {"miFormulario": miFormulario, "estudiante_nombre": estudiante_nombre})







from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "app/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "app/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "app/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "app/login.html", {"form": form})





# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"app/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"app/registro.html" ,  {"form":form})