from rest_framework import serializers
from .models import User
from . import models
from farmers import serializers as farmers_serializers


class UserAccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class UserAccountSerializer(serializers.ModelSerializer):
    # farmer = farmers_serializers.FarmerAccountSerializer(
    #     read_only=True, required=False)
    farmer = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')




class PublicUserAccountListSerializer(serializers.ModelSerializer):
    # farmer = farmers_serializers.PublicFarmerSerializer(read_only=True, required=False)
    farmer = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'date_joined', 'farmer')


# class PublicUserAccountSerializer(serializers.ModelSerializer):
#     farmer = farmers_serializers.PublicFarmerDetailSerializer(read_only=True, required=False)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'first_name',
#                   'last_name', 'date_joined', 'farmer')
