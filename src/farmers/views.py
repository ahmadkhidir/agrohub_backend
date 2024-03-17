from rest_framework import generics, permissions, status, exceptions
from rest_framework.request import Request
from . import serializers
from .models import User
from . import models
from utilities import status as util_status


class FarmerAccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for viewing, updating and delete farmer account.
    """
    queryset = models.Farmer.objects.all()
    serializer_class = serializers.FarmerAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        try:
            return self.request.user.farmer
        except models.Farmer.DoesNotExist:
            raise exceptions.NotFound(util_status.NOT_FOUND)


class FarmerAccountCreateAPIView(generics.CreateAPIView):
    """
    This view is for creating farmer account.
    """
    queryset = models.Farmer.objects.all()
    serializer_class = serializers.FarmerAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class FarmAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for viewing, updating and delete farm.
    """
    queryset = models.Farm.objects.all()
    serializer_class = serializers.FarmSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        obj: models.Farm = super().get_object()
        user = self.request.user
        if obj.owner.user == user:
            return obj
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


class FarmCreateAPIView(generics.CreateAPIView):
    """
    This view is for creating farm.
    """
    queryset = models.Farm.objects.all()
    serializer_class = serializers.FarmCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        try:
            owner = self.request.user.farmer
        except models.Farmer.DoesNotExist:
            raise exceptions.NotFound(util_status.NOT_FOUND)
        else:
            return serializer.save(owner=owner)


class FarmLocationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for viewing, updating and delete farm location.
    """
    queryset = models.FarmLocation.objects.all()
    serializer_class = serializers.FarmLocationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        obj: models.FarmLocation = super().get_object()
        user = self.request.user
        if obj.farm.owner.user == user:
            return obj
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


class FarmLocationCreateAPIView(generics.CreateAPIView):
    """
    This view is for creating farm location.
    """
    queryset = models.FarmLocation.objects.all()
    serializer_class = serializers.FarmLocationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        farm = serializer.validated_data.get('farm')
        if user == farm.owner.user:
            return serializer.save()
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


class FarmPhotoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for viewing, updating and delete farm photo.
    """
    queryset = models.FarmPhoto.objects.all()
    serializer_class = serializers.FarmPhotoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        obj: models.FarmPhoto = super().get_object()
        user = self.request.user
        if obj.farm.owner.user == user:
            return obj
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


class FarmPhotoCreateAPIView(generics.CreateAPIView):
    """
    This view is for creating farm photo.
    """
    queryset = models.FarmPhoto.objects.all()
    serializer_class = serializers.FarmPhotoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        farm = serializer.validated_data.get('farm')
        if user == farm.owner.user:
            return serializer.save()
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)

