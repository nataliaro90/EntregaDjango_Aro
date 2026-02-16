from django.urls import path
from blog import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor-formulario/', views.formulario_autor, name="FormularioAutor"),
    path('buscar/', views.buscar, name="Buscar"),
    path('buscar-resultados/', views.resultados_busqueda, name="ResultadosBusqueda"),
]