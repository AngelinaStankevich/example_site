from django.urls import path, include
from rest_framework import routers

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

from . import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('votes', views.VoteViewSet)
router.register('tags', views.TagViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path('docs/swagger<format>/', schema_view.without_ui(cache_timeout=0),
                 name='schema-json'),
            path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0),
                 name='schema-swagger-ui'),
            path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
                 name='schema-redoc'),
        ]
    )



