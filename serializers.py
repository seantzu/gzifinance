from rest_framework import serializers
from .models import *


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class FindataAttributeSerializer(serializers.ModelSerializer):
    class Meta():
        model = FindataAttribute
        exclude = ('id', 'GZIDATA',)


class GetDataSerializer(serializers.ModelSerializer):
    FINDATA = serializers.SerializerMethodField()

    def get_FINDATA(self, obj):
        qs = FindataAttribute.objects.filter(GZIDATA_id=obj.pk)
        serializer = FindataAttributeSerializer(instance=qs, many=True)
        return serializer.data

    class Meta():
        model = GZIDATA
        fields = ('UNDERLYING', 'SECTYPE', 'EXCHANGE',
                  'BIODATA', 'CRYPTODATA', 'FINDATA',)

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta():
        model = UploadedFile
        fields = '__all__'