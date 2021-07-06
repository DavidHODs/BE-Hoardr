"""hoarder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from hoarding_app.views import ItemViewSet, ImageViewSet, FreeExerciseViewSet, ItemIDViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Hoarder App API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      # contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'itemize', ItemIDViewSet, 'item')
router.register(r'items', ItemViewSet)
router.register(r'images', ImageViewSet)
router.register(r'free_exercises', FreeExerciseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/auth', include('authentication.urls')),
    path('api/auth', include('direct_message.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]
