from django.urls import path
from mi_app.views import *

urlpatterns = [
    path('',inicio, name = 'Inicio'),
    path('cursos/', curso, name = 'Curso'),
    path('estudiantes/', estudiantes, name = 'Estudiantes'),
    path('profesores/',profesores, name = 'Profesores'),
    path('entregables/',entregables, name = 'Entregables'),
    # path('cursoformulario', cursoFormulario, name='CursoFormulario'),
    # path('profesoresformulario', profesoresformulario, name='ProfesoresFormulario'),
    # path('estudiantesformulario', estudiantesformulario, name='EstudiantesFormulario'),
    # path('entregablesformulario', entregablesformulario, name='EntregablesFormulario'),
    path('buscarcamada/', busquedacamada, name='busquedaCamada'),
    path('buscar/', buscar),
    path('leerprofesores', leerProfesores, name = "LeerProfesores"),
    path('eliminarprofesor/<profesor_nombre>/', eliminarProfesor, name="eliminarprofesor"),
    path('editarprofesor/<profesor_nombre>/', editarProfesor, name='editarprofesor'),
    path('leercursos', leerCursos, name = "leercursos"),
    path('eliminarcurso/<curso_nombre>/', eliminarCurso, name="eliminarcurso"),
    path('editarcurso/<curso_nombre>/', editarCurso, name='editarcurso'),
    path('leerestudiantes', leerEstudiantes, name = "leerestudiantes"),
    path('eliminarestudiante/<estudiante_nombre>/', eliminarEstudiantes, name="eliminarestudiante"),
    path('editarestudiante/<estudiante_nombre>/', editarEstudiante, name='editarestudiante'),



    path('login', login_request, name= 'login'),
    path('registro', register, name='Registro'),

]