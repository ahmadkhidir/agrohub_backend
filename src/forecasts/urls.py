from django.urls import path
from . import views


urlpatterns = [
    path("crops/recommendation/", views.CropRecommendationAPIView.as_view(),
         name="crops_recommendation")
]
