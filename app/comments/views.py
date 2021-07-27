from re import search
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogPostSerializer, CommentsSerializer
from .serializers import CommentsThreeInPost, CommentsThree, PostSerializerPost
from .models import Post, Comments


class PostSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializerPost
    http_method_names = ['get', 'post']

    def list(self, request):
        post = Post.objects.all()
        serializer = BlogPostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PostSerializerPost(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentsSet(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    http_method_names = ['get', 'post']

    def list(self, request):
        commetns = Comments.objects.all()
        serializer = CommentsSerializer(commetns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentParentChildren(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsThree
    http_method_names = ['get']

    def list(self, request):
        commetns = Comments.objects.all()
        serializer = CommentsThree(commetns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostShowThreeComments(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = CommentsThreeInPost
    http_method_names = ['get']

    def list(self, request):
        post = Post.objects.all()
        serializer = CommentsThreeInPost(post, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = CommentsThreeInPost(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

