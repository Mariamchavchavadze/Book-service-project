"""
URL configuration for book_lending_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# book_lending_service/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Import the schema view for Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Create a simple view for the home route
def home_view(request):
    return HttpResponse("Welcome to the Book Lending Service API! Please visit /swagger/ for the API documentation.")


# Define the schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Book Lending Service API",
        default_version='v1',
        description="API for managing book lending service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@booklending.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Home URL
    path('', home_view, name='home'),  # This is the root URL '/' route

    # Admin page URL
    path('admin/', admin.site.urls),

    # API endpoints (Books, Authors, Genres, etc.)
    path('api/', include('books.urls')),  # All API endpoints

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
