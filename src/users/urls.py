from django.urls import path
from . import views


urlpatterns = [
    # User profile
    path('profile/public/', views.PublicUserAccountListAPIView.as_view(), name='public_user_list'),
    path('profile/public/<slug:pk>/', views.PublicUserAccountAPIView.as_view(), name='public_user_detail'),
    path('profile/', views.UserAccountAPIView.as_view(), name='personal_user_detail'),
    # Account creation
    path('account/create/', views.UserAccountCreateAPIView.as_view(), name='regular_account_create'),
    
]
