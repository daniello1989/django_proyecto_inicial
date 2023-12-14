from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Autor, Poema
from .forms import CrearNuevoPoema, CrearnNuevoProyecto, CrearNuevoAutor

# Create your views here.
def home(request):
    return render(request, "home.html")
    #return HttpResponse("Hello world!"+nombreusuario)

def about(request):
    titulo = "P0EMAR.io"
    return render(request, "about.html", {
        'titulo': titulo
        })

def home_2(request, id):
    print(type(id))
    return HttpResponse("<h1>Has seleccionado el poema con id:  %s</h1>" %id)

def user(request):
    return render(request, "user_home.html")


#********************GETS****************************************************************
#PROYECTO
def proyecto_template(request):
    titulo = "Mis proyectos"
    proyectos= list(Proyecto.objects.values())
    return render(request, "proyecto.html",{
        'proyectos':proyectos,
        'titulo': titulo
    })

def proyecto_GetAll(request):
    proyectos= list(Proyecto.objects.values())
    return JsonResponse(proyectos, safe=False)

def proyecto_GetOne(request, id):
    #proyecto=Proyecto.objects.get(id=id)
    proyecto= get_object_or_404(Proyecto, id=id)
    return HttpResponse("El proyecto seleccionado es el siguiente: %s" %proyecto.nombre)

def proyecto_GetOne_titulo(request, nombre):
    #proyecto=Proyecto.objects.get(id=id)
    proyecto= get_object_or_404(Proyecto, nombre=nombre)
    return HttpResponse("El proyecto seleccionado es el siguiente: %s" %proyecto.nombre)

#Sacar todos los proyectos/libros de un autor
def proyecto_Get_libro_porautor(request, id):
    id_autor=id
    libros= list(Proyecto.objects.values())
    libros_por_autor=[]

    for l in libros: 
        for k, v in l.items():
            if k == 'autor_id' and v == id_autor:
                libros_por_autor.append(l)
                #print(k,v)
    
    autor= get_object_or_404(Autor, id=id_autor)
    return render(request, "proyecto.html",{
        'proyectos': libros_por_autor,
        'titulo': autor.nombre
        })

#***************CREAR NUEVO PROYECTO*****************************
def crear_proyecto(request):
    if request.method == 'GET':
        return render(request, 'crear_proyecto.html', {
            'formulario': CrearnNuevoProyecto
        })
    else:
        Proyecto.objects.create(nombre=request.POST['nombre'])
        return redirect('proyectos')


#***************POEMAS*******************************************
def poema_template(request):
    titulo="Mis poemas guardados"
    poemas= list(Poema.objects.values())
    return render(request, "poema.html",{
        'poemas': poemas,
        'titulo': titulo
    })

def poema_GetAll(request):
    poemas= list(Poema.objects.values())
    return JsonResponse(poemas, safe=False)

def poema_GetOne(request, id):
    #poema=Poema.objects.get(id=id)
    poema= get_object_or_404(Poema, id=id)
    return HttpResponse("El poema seleccionado es el siguiene: %s" %poema.titulo)
 
def poema_GetOne_titulo(request, nombre):
    poema=Poema.objects.get(titulo=nombre)
    return HttpResponse("El poema seleccionado es el siguiene: %s" %poema.titulo)

#Sacar todos los poemas de un libro
def poema_Get_poemas_libro(request, id):
    id_libro=id
    poemas= list(Poema.objects.values())
    poemas_por_libro=[]

    for p in poemas: 
        for k, v in p.items():
            if k == 'proyecto_id' and v == id_libro:
                poemas_por_libro.append(p)
                #print(k,v)
    
    libro= get_object_or_404(Proyecto, id=id_libro)
    return render(request, "poema_por_libro.html",{
        'poemas': poemas_por_libro,
        'titulo': libro.nombre
        })

#Sacar todos los poemas de un autor
def poema_Get_poemas_porautor(request, id):
    id_autor=id
    poemas= list(Poema.objects.values())
    poemas_por_autor=[]

    for p in poemas: 
        for k, v in p.items():
            if k == 'autor_id' and v == id_autor:
                poemas_por_autor.append(p)
                #print(k,v)
    
    autor= get_object_or_404(Autor, id=id_autor)
    return render(request, "poema.html",{
        'poemas': poemas_por_autor,
        'titulo': autor.nombre
        })

#CREAR POEMA
#Crear un nuevo poema
def crear_poema(request):

    if request.method == 'GET':
        return render(request, 'crear_poema.html', {
        'formulario': CrearNuevoPoema()
        })
    else:
        Poema.objects.create(titulo=request.POST['titulo'], 
        contenido=request.POST['contenido'], 
        descripcion=request.POST['descripcion'],
        proyecto_id=2)

        return redirect('poemas')

#Eliminar un poema
def eliminar_poema_id(request, id):
    id_poema=id
    try:
        poema = Poema.objects.get(id=id_poema)
        poema.delete()
        return redirect('eliminado')

    except:
        return redirect('error_eliminado')
    


def autores(request):
    titulo="Mis autores favoritos"
    autores= list(Autor.objects.values())
    return render(request, "autor.html",{
        'autores': autores,
        'titulo': titulo
    })

#Crear un nuevo autor
def crear_autor(request):

    titulo= "Crea un nuevo usuario"
    if request.method =='GET':
        return render(request, "crear_autor.html",{
            'formulario': CrearNuevoAutor(),
            'titulo': titulo
        })
    else:
        Autor.objects.create(nombre=request.POST['nombre'],
        biografia= request.POST['biografia'])

        return redirect('autores')

#Eliminado y error_eliminado
def eliminado (request):
    return render(request, "eliminado.html")

def error_eliminado (request):
    return render(request, "error_eliminado.html")