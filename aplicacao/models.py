from django.db import models

class Video(models.Model):
    class Meta:
        db_table = 'video'

    titulo = models.CharField(max_length=200) 
    descricao = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
