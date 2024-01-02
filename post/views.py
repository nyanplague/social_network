from django.shortcuts import render
from rest_framework import mixins, viewsets
from post.serializers import PostSerializer
from post.models import Post


class PostViewSet(
    viewsets.ModelViewSet
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
