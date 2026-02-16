from django import forms

class AutorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class PostForm(forms.Form):
    titulo = forms.CharField()
    contenido = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField(widget=forms.SelectDateWidget)

class CategoriaForm(forms.Form):
    nombre = forms.CharField()