from django.contrib import admin
from aplicacao.models import Video, Categoria

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')

class Videos(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'url')

admin.site.register(Categoria, Categorias)
admin.site.register(Video, Videos)


