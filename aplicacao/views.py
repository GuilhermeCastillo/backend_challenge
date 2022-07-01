from django.shortcuts import render
from rest_framework import generics, serializers, viewsets
from aplicacao.models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer, VideoCategoriaSerializer

class VideoCategoriaList(generics.ListAPIView):
    def get_queryset(self):
        categoriaId_value = self.kwargs['pk']
        return Video.objects.filter(categoriaId=categoriaId_value)
        
    serializer_class = VideoCategoriaSerializer

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
