from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Entregable)


admin.site.site_header = 'Mi aplicacion'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Admnistración'