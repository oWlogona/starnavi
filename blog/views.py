from django.db.models import F
from django.http import Http404
from rest_framework import status
from blog.models import Blog, Like
from rest_framework.views import APIView
from blog.serializers import BlogSerializer
from rest_framework.response import Response
from blog.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        blog_list = Blog.objects.all()
        serializer = BlogSerializer(blog_list, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogDetail(APIView):

    def get_object(self, pk):
        try:
            return get_object_or_404(Blog, pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogLike(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        like, created = Like.objects.get_or_create(author=request.user, post_id=kwargs['pk'])
        if created:
            Blog.objects.filter(id=kwargs['pk']).update(like_count=F('like_count') + 1)
        else:
            Blog.objects.filter(id=kwargs['pk']).update(like_count=F('like_count') - 1)
            like.delete()
        blog = Blog.objects.filter(id=kwargs['pk'])
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
