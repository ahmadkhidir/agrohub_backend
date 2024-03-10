from rest_framework_simplejwt import views as jwt
from rest_framework import views, permissions, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from . import serializers

class BasicAuthView(jwt.TokenObtainPairView):
    pass

class BasicAuthRefreshView(jwt.TokenRefreshView):
    pass

class BasicAuthVerifyView(jwt.TokenVerifyView):
    pass

class BasicAuthChangePassword(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BasicAuthChangePasswordSerializer
    

    @swagger_auto_schema(
            request_body=serializer_class,
            responses={
                status.HTTP_200_OK: serializer_class,
            }
    )
    def post(self, request: Request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            old_password= serializer.validated_data.get('old_password')
            new_password= serializer.validated_data.get('new_password')
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({
                "detail": "The old password is not correct"
            }, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)