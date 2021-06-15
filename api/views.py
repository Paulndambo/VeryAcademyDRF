from django.shortcuts import render
from data.models import Category, Post
from rest_framework import generics 
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly 
# Create your views here.
class PostUserWritePermission(BasePermission):
  message = "Post can only be edited by author"

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True
    return obj.author == request.user




class PostList(generics.ListCreateAPIView):
    #permission_classes = [IsAdminUser]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [DjangoModelPermissions]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
