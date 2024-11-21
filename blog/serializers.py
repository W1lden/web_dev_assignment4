from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'timestamp']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Для отображения имени автора

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'timestamp', 'comments']
