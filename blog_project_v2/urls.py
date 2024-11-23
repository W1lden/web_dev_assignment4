from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from django.conf.urls.static import static

# Настройка для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API by W1lden",
        default_version='v1',
        description="API documentation for the Blog project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="Asan.Bitanov@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,),  # Добавьте эту строку
)


urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    
    # Маршруты API
    # path('api/', include('blog.urls')),

    # Версии API
    path('api/v1/', include('blog.urls')),  # Версия 1
    path('api/v2/', include('blog.urls')),  # Версия 2

    # JWT-токены
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger и ReDoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)