from django.urls import path
from miaplicacion import views

urlpatterns= [
    path("miaplicacion/", views.home, name="index"),
    path("about/", views.about, name="sobre_nosotros"),
    path("home/<int:id>", views.home_2, name="home"),
    path("proyecto/", views.proyecto_GetAll, name="proyecto"),
    path("poema/", views.poema_GetAll, name="poema"),
    path("proyecto/<int:id>", views.proyecto_GetOne, name="proyecto_unico_id"),
    path("proyecto/<str:nombre>", views.proyecto_GetOne_titulo, name="proyecto_unico_nombre"),
    path("proyecto/crear/", views.crear_proyecto, name="crear_proyecto"),
    path("poema/<int:id>", views.poema_GetOne, name="poema_unico_id"),
    path("poema/<str:nombre>", views.poema_GetOne_titulo, name="poema_unico_nombre"),
    path("proyecto_template/", views.proyecto_template, name="proyectos"),
    path("poema_template/", views.poema_template, name="poemas"),
    path("poema/crear/", views.crear_poema, name="crear_poema"),
    path("user/", views.user, name="vista_usuario"),
    path("autores/", views.autores, name="autores"),
    path("autores/crear", views.crear_autor, name="crear_autor"),
    path("poemas/libro/<int:id>", views.poema_Get_poemas_libro, name="poemas_libro"),
    path("poemas/autor/<int:id>", views.poema_Get_poemas_porautor, name="poemas_autor"),
    path("proyecto/autor/<int:id>", views.proyecto_Get_libro_porautor, name="proyecto_autor"),
    path("poema/eliminar/<int:id>", views.eliminar_poema_id, name="eliminar_poema_porid"),
    path("eliminado/", views.eliminado, name="eliminado"),
    path("error_eliminado/", views.error_eliminado, name="error_eliminado")

    #path("home/<str:nombreusuario>", views.home_2, name="home_2")
    ]