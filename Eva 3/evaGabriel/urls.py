"""
URL configuration for evaGabriel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from entrada import views as app1
from clientes import views as app2
from peliculas import views as app3

app_name = 'entrada'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.pagina_principal, name='pagina_principal'),

    # URLs de la app1 (Entrada)
    path('listar_entradas/', app1.listar_entradas, name='listar_entradas'),
    path('registrar_entrada/', app1.registrar_entrada, name='registrar_entrada'),
    path('editar_entrada/<int:id>/', app1.editar_entrada, name='editar_entrada'),
    path('eliminar_entrada/<int:entrada_id>/', app1.eliminar_entrada, name='eliminar_entrada'),

    # URLs de la app2 (Cliente)
    path('listar_clientes/', app2.listar_clientes, name='listar_clientes'),
    path('registrar_cliente/', app2.registrar_cliente, name='registrar_cliente'),
    path('editar_cliente/<int:id>/', app2.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', app2.eliminar_cliente, name='eliminar_cliente'),

    # URLs de la app3 (Pelicula)
    path('listar_peliculas/', app3.listar_peliculas, name='listar_peliculas'),
    path('registrar_pelicula/', app3.registrar_pelicula, name='registrar_pelicula'),
    path('editar_pelicula/<int:id>/', app3.editar_pelicula, name='editar_pelicula'),
    path('eliminar_pelicula/<int:pelicula_id>/', app3.eliminar_pelicula, name='eliminar_pelicula'),
]

