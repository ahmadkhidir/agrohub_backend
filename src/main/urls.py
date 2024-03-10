from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AgroHub API",
        default_version='v1',
        description="""AgroHub is a Unified Agricultural Hub 
        that is designed to provide a comprehensive solutions for farmers, 
        integrating agricultural weather forcasting, farm equipment sharing, 
        and a marketplace for sustainable agricultural products.""",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="khidirahmad05@gmail.com", 
                                name="Ahmad Khidir", 
                                url="https://linkedin.com/in/ahmadkhidir/"),
        license=openapi.License(name="AgroHub License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # app urls
    path("users/", include('users.urls'), name="users"),
    path("auth/", include('api_auth.urls'), name="auth"),
    # rest_framework urls
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('accounts/', include('rest_framework.urls')),
    # platform urls
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
