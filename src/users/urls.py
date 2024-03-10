from django.urls import path
from . import views


urlpatterns = [
    # User profile
    path('profile/public/', views.PublicUserListView.as_view(), name='public_user_list'),
    path('profile/public/<slug:pk>/', views.PublicUserDetailView.as_view(), name='public_user_detail'),
    path('profile/personal/', views.PersonalUserDetailView.as_view(), name='personal_user_detail'),
    # Account creation
    path('account/regular/create/', views.CreateRegularAccountAPIView.as_view(), name='regular_account_create'),
    path('account/farmer/create/', views.FarmerAccountCreateAPIView.as_view(), name='farmer_account_create'),
    path('account/farmer/<slug:pk>/', views.FarmerAccountAPIView.as_view(), name='farmer_account'),
    path('account/farmer/farm/create/', views.FarmCreateAPIView.as_view(), name='farmer_farm_create'),
    path('account/farmer/farm/<slug:pk>/', views.FarmAPIView.as_view(), name='farmer_farm'),
    path('account/farmer/farm/location/create/', views.FarmLocationCreateAPIView.as_view(), name='farmer_location_create'),
    path('account/farmer/farm/location/<slug:pk>/', views.FarmLocationAPIView.as_view(), name='farmer_location'),
    path('account/farmer/farm/photos/create/', views.FarmPhotoCreateAPIView.as_view(), name='farmer_photos_create'),
    path('account/farmer/farm/photos/<slug:pk>/', views.FarmPhotoAPIView.as_view(), name='farmer_photos'),
]
