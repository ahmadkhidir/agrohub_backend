from django.urls import path
from . import views


urlpatterns = [
    # Farmer Account
    path('account/create/', views.FarmerAccountCreateAPIView.as_view(), name='farmer_account_create'),
    path('account/farm/create/', views.FarmCreateAPIView.as_view(), name='farmer_farm_create'),
    path('account/farm/location/create/', views.FarmLocationCreateAPIView.as_view(), name='farmer_location_create'),
    path('account/farm/photos/create/', views.FarmPhotoCreateAPIView.as_view(), name='farmer_photos_create'),
    # Farmer Profile
    path('profile/', views.FarmerAccountAPIView.as_view(), name='farmer_account'),
    path('profile/farm/<slug:pk>/', views.FarmAPIView.as_view(), name='farmer_farm'),
    path('profile/farm/location/<slug:pk>/', views.FarmLocationAPIView.as_view(), name='farmer_location'),
    path('profile/farm/photos/<slug:pk>/', views.FarmPhotoAPIView.as_view(), name='farmer_photos'),
]
