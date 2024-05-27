from rest_framework import serializers
from . import models

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FarmCrop
        fields = ['id', 'name', 'photo']

class FarmPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FarmPhoto
        fields = '__all__'
        extra_kwargs = {'farm': {'write_only': True}}

class FarmLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FarmLocation
        fields = '__all__'
        extra_kwargs = {'farm': {'write_only': True}}

class FarmSerializer(serializers.ModelSerializer):
    crops = CropSerializer(many=True, required=False, read_only=True)
    photos = FarmPhotoSerializer(many=True, source="farmphoto_set", required=False, read_only=True)
    location = FarmLocationSerializer(required=False, source='farmlocation', read_only=True)
    class Meta:
        model = models.Farm
        fields = '__all__'
        extra_kwargs = {'owner': {'write_only': True}}

class FarmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farm
        exclude = ['owner']
        # fields = '__all__'
        # extra_kwargs = {'owner': {'write_only': True}}


class FarmerAccountSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(many=True, required=False, source='farm_set', read_only=True)
    class Meta:
        model = models.Farmer
        exclude = ['user']
        # fields = '__all__'
        # extra_kwargs = {'user': {'write_only': True}}

class PublicFarmerAccountListSerializer(serializers.ModelSerializer):
    farm_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Farmer
        exclude = ['user']

    def get_farm_count(self, obj: models.Farmer):
        return obj.farm_set.count()


class PublicFarmerAccountDetailSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(
        many=True, required=False, source='farm_set', read_only=True)

    class Meta:
        model = models.Farmer
        exclude = ['user']
