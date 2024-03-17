from rest_framework import generics, permissions, status, exceptions
from rest_framework.request import Request
from . import serializers
from .models import User
from . import models
from utilities import status as util_status


class PublicUserAccountListAPIView(generics.ListAPIView):
    """
    This view is for listing users public profile.
    """
    queryset = User.objects.all()
    serializer_class = serializers.PublicUserAccountListSerializer
    permission_classes = (permissions.AllowAny,)


class PublicUserAccountAPIView(generics.RetrieveAPIView):
    """
    This view is for viewing selected users (using username field) public profile.
    """
    queryset = User.objects.all()
    serializer_class = serializers.PublicUserAccountListSerializer
    permission_classes = (permissions.AllowAny,)


class UserAccountAPIView(generics.RetrieveUpdateAPIView):
    """
    This view is for viewing, updating current user profile.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserAccountCreateAPIView(generics.CreateAPIView):
    """
    This view is for creating user account.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserAccountCreateSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return user



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
