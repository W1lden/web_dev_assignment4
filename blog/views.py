from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# View для списка постов и создания нового поста
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View для получения, обновления или удаления конкретного поста
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View для комментариев
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Убедимся, что post_id передается и создается связанный комментарий
        serializer.save()

# View для получения, обновления или удаления конкретного комментария
class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
