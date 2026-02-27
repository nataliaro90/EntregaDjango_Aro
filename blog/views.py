from django.shortcuts import render
from .models import Autor, Post, Categoria
from .forms import AutorForm, PostForm, CategoriaForm

# 1. Vista de Inicio
# Esta función simplemente muestra la página principal del blog.
def inicio(request):
    return render(request, "blog/inicio.html")

# 2. Formulario para Autor
# Procesa el envío de datos y guarda un nuevo Autor en la base de datos.
def formulario_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            # Se crea la instancia del modelo y se guarda
            autor = Autor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            autor.save()
            return render(request, "blog/inicio.html", {"mensaje": "Autor guardado con éxito"})
    else:
        form = AutorForm()
    return render(request, "blog/formulario_autor.html", {"form": form})

# 3. Formulario para Post
# Recibe los datos del formulario de Post y los persiste en la DB.
def formulario_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            # Se crea la instancia del modelo Post
            post = Post(titulo=info['titulo'], contenido=info['contenido'], fecha=info['fecha'])
            post.save()
            return render(request, "blog/inicio.html", {"mensaje": "Post publicado con éxito"})
    else:
        form = PostForm()
    return render(request, "blog/formulario_post.html", {"form": form})

# 4. Formulario para Categoria
# Permite crear nuevas categorías para el blog.
def formulario_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            # Se guarda la categoría en la tabla correspondiente
            categoria = Categoria(nombre=info['nombre'])
            categoria.save()
            return render(request, "blog/inicio.html", {"mensaje": "Categoría creada con éxito"})
    else:
        form = CategoriaForm()
    return render(request, "blog/formulario_categoria.html", {"form": form})

# 5. Búsqueda
# 'buscar' muestra la página del buscador, 'resultados_busqueda' filtra por título.
def buscar(request):
    return render(request, "blog/buscar.html")

def resultados_busqueda(request):
    titulo_buscado = request.GET.get("titulo")
    if titulo_buscado:
        # Filtra los posts cuyo título contenga la palabra buscada
        posts = Post.objects.filter(titulo__icontains=titulo_buscado)
        return render(request, "blog/resultados_busqueda.html", {"posts": posts, "titulo": titulo_buscado})

    return render(request, "blog/inicio.html", {"respuesta": "No enviaste datos"})