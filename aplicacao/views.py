from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from aplicacao.models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer, VideoCategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class VideoCategoriaList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        categoriaId_value = self.kwargs['pk']
        return Video.objects.filter(categoriaId=categoriaId_value)    
    
    serializer_class = VideoCategoriaSerializer

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo']
    search_fields = ['titulo']

class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias"""
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer 
    
