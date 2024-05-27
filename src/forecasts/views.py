from rest_framework.views import APIView
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from rest_framework.response import Response
from rest_framework.request import Request
import requests as http_requests


class CropRecommendationAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class= serializers.CropRecommendationRequestSerializer

    @swagger_auto_schema(
            request_body=serializer_class
    )
    def post(self, requests: Request, *args, **kwargs):
        data = self.serializer_class(data=requests.data)
        data.is_valid(raise_exception=True)
        data = {k.title(): v for k,v in data.validated_data.items()}
        response = http_requests.post("http://ai:8001/", json=data)
        return Response(data=response.json(), status=response.status_code)