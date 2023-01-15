from django.urls import path
from mi_app.views import *

urlpatterns = [
    path('',inicio, name = 'Inicio'),
    path('cursos/', curso, name = 'Curso'),
    path('estudiantes/', estudiantes, name = 'Estudiantes'),
    path('profesores/',profesores, name = 'Profesores'),
    path('entregables/',entregables, name = 'Entregables'),
    path('cursoformulario', cursoFormulario, name='CursoFormulario'),
    path('profesoresformulario', profesoresformulario, name='ProfesoresFormulario'),
    path('estudiantesformulario', estudiantesformulario, name='EstudiantesFormulario'),
    path('entregablesformulario', entregablesformulario, name='EntregablesFormulario'),



]