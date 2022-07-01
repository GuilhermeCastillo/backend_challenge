from rest_framework import serializers

from .models import Categoria, Video

class VideoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    

# Show all of the PASSENGERS in particular WORKSPACE
    # or all of the PASSENGERS in particular AIRLINE
    # def get_queryset(self):
    #     queryset = Video.objects.all()
    #     workspace = self.request.query_params.get('videos')

    #     if workspace:
    #         queryset = queryset.filter(titulo=workspace)

    #     return queryset

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
