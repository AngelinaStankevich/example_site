from rest_framework import viewsets, filters, pagination
from django.conf import settings

from . import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = settings.DEFAULT_PAGE_SIZE
    max_limit = settings.MAX_PAGE_SIZE


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['pub_date']


class VoteViewSet(viewsets.ModelViewSet):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    pagination_class = LimitOffsetPagination

