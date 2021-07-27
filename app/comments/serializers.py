from rest_framework import serializers
from .models import Post, Comments


class RecursivSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class BlogPostSerializer(serializers.ModelSerializer):
    comment = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields= ('id', 'title', 'body', 'comment')


class PostSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields= ('id', 'title', 'body',)


class CommentsThree(serializers.ModelSerializer):
    children = RecursivSerializer(many=True)

    class Meta:
        model = Comments
        fields = ('id', 'post', 'email', 'text', 'parent', 'children')


class CommentsThreeInPost(serializers.ModelSerializer):
    comment = CommentsThree(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'comment')


class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = '__all__'
