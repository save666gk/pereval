from rest_framework import serializers
from .models import Pereval, PerevalImage

class PerevalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImage
        fields = ['title', 'image']

class PerevalSerializer(serializers.ModelSerializer):
    images = PerevalImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        pereval = Pereval.objects.create(**validated_data)
        for image_data in images_data:
            PerevalImage.objects.create(pereval=pereval, **image_data)
        return pereval
