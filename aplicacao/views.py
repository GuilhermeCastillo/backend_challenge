from django.shortcuts import render
from rest_framework import generics, viewsets
from aplicacao.models import Video
from .serializers import VideoSerializer

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
