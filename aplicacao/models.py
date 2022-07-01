from django.db import models

class Categoria(models.Model):
    class Meta:
        db_table = 'categoria'

    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
   
    def __str__(self):
        return self.titulo

class Video(models.Model):
    class Meta:
        db_table = 'video'

    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    # relacionamento
    categoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo
