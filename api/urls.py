from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

