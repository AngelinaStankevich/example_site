from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'url', 'title', 'body', 'author', 'pub_date', 'tags']


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vote
        fields = ['id', 'url', 'voter', 'post', 'up']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['id', 'url', 'title', 'posts']