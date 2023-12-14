from django.contrib import admin
from .models import Proyecto, Poema, Autor

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Poema)
admin.site.register(Autor)