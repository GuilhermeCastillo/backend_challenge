from rest_framework import serializers

from .models import Categoria, Video

class VideoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
   
    # def get_periodo(self, obj):
    #     return obj.get_periodo_display()

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
