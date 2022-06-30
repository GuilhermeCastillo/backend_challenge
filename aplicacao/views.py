from django.shortcuts import render
from rest_framework import generics, serializers, viewsets
from aplicacao.models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
