from django import forms

class CrearNuevoPoema(forms.Form): 
    titulo = forms.CharField(label= "Título del poema",max_length=200, required=True)
    contenido = forms.CharField(label="Escribe aquí tu poema", widget=forms.Textarea)
    descripcion= forms.CharField(label="Descripción de tu poema", widget=forms.Textarea)

class CrearnNuevoProyecto(forms.Form):
    nombre= forms.CharField(label= "Título de tu nuevo proyecto literario",max_length=200, required=True)

class CrearNuevoAutor(forms.Form):
    nombre = forms.CharField(label="Introduce el nombre del autor", max_length=200, required=True)
    biografia= forms.CharField(label="Biografía del autor", widget=forms.Textarea, required=True) 
