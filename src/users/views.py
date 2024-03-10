from rest_framework import generics, permissions, status, exceptions
from rest_framework.request import Request
from . import serializers
from .models import User
from . import models
from utilities import status as util_status


class PublicUserListView(generics.ListAPIView):
    """
    This view is for listing users public profile.
    """
    queryset = User.objects.all()
    serializer_class = serializers.PublicUserSerializer
    permission_classes = (permissions.AllowAny,)


class PublicUserDetailView(generics.RetrieveAPIView):
    """
    This view is for viewing selected users (using username field) public profile.
    """
    queryset = User.objects.all()
    serializer_class = serializers.PublicUserDetailSerializer
    permission_classes = (permissions.AllowAny,)


class PersonalUserDetailView(generics.RetrieveUpdateAPIView):
    """
    This view is for viewing, updating current user profile.
    """
    queryset = User.objects.all()
    serializer_class = serializers.PersonalUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class CreateRegularAccountAPIView(generics.CreateAPIView):
    """
    This view is for creating user account.
    """
    queryset = User.objects.all()
    serializer_class = serializers.RegularAccountSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return user


class FarmerAccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for viewing, updating and delete farmer account.
    """
    queryset = models.Farmer.objects.all()
    serializer_class = serializers.FarmerAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        obj: models.Farmer = super().get_object()
        user = self.request.user
        if obj.user == user:
            return obj
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


class FarmerAccountCreateAPIView(generics.CreateAPIView):
    """
    This view is for creating farmer account.
    """
    queryset = models.Farmer.objects.all()
    serializer_class = serializers.FarmerAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        if user == serializer.validated_data.get('user'):
            return serializer.save()
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


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
    serializer_class = serializers.FarmSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        farmer = serializer.validated_data.get('owner')
        if user == farmer.user:
            return serializer.save()
        raise exceptions.AuthenticationFailed(util_status.NO_ACCESS)


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


# class CropAPIView(generics.CreateAPIView):
#     """
#     This view is for creating crop.
#     """
#     queryset = models.Crop.objects.all()
#     serializer_class = serializers.CropSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     # def perform_create(self, serializer):
#     #     crop = serializer.save()
#     #     return crop


# class CropDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     This view is for viewing, updating and delete crop.
#     """
#     queryset = models.Crop.objects.all()
#     serializer_class = serializers.CropSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def perform_update(self, serializer):
#         crop = serializer.save()
#         return crop
