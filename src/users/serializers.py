from rest_framework import serializers
from .models import User
from . import models


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Crop
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


class FarmerAccountSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(many=True, required=False, source='farm_set', read_only=True)
    class Meta:
        model = models.Farmer
        fields = '__all__'
        extra_kwargs = {'user': {'write_only': True}}


class RegularAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class PersonalUserSerializer(serializers.ModelSerializer):
    farmer = FarmerAccountSerializer(read_only=True, required=False)
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')
        

class PublicFarmerSerializer(serializers.ModelSerializer):
    farm_count = serializers.SerializerMethodField()
    class Meta:
        model = models.Farmer
        exclude = ['user']
    
    def get_farm_count(self, obj: models.Farmer):
        return obj.farm_set.count()


class PublicFarmerDetailSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(many=True, required=False, source='farm_set', read_only=True)
    class Meta:
        model = models.Farmer
        exclude = ['user']


class PublicUserSerializer(serializers.ModelSerializer):
    farmer = PublicFarmerSerializer(read_only=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 
                  'last_name', 'date_joined', 'farmer')


class PublicUserDetailSerializer(serializers.ModelSerializer):
    farmer = PublicFarmerDetailSerializer(read_only=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 
                  'last_name', 'date_joined', 'farmer')
