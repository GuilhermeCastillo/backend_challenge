from django.contrib import admin
from aplicacao.models import Video

class Videos(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'url')

admin.site.register(Video, Videos)

