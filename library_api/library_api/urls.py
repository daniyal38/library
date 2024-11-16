from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="API for managing a library's books",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Public access to documentation
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/',include('books.urls')),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),  # Swagger UI
]
