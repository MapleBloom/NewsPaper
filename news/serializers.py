from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = Post
        fields = ['url', 'id', 'post', 'time_in', 'title', 'text', 'rating', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'id', 'user', 'post', 'time_in', 'text', 'rating']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'comments']
