from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor-formulario/', views.formulario_autor, name="FormularioAutor"),
    path('post-formulario/', views.formulario_post, name="FormularioPost"),
    path('categoria-formulario/', views.formulario_categoria, name="FormularioCategoria"),
    path('buscar/', views.buscar, name="Buscar"),
    path('buscar-resultados/', views.resultados_busqueda, name="ResultadosBusqueda"),
]