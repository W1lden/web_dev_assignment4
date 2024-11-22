from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('comments').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Разрешение для постов

    def perform_create(self, serializer):
        # Автором поста автоматически становится текущий пользователь
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Разрешение для комментариев

    def perform_create(self, serializer):
        # Автором комментария автоматически становится текущий пользователь
        serializer.save(author=self.request.user)

class PostViewSetV2(ModelViewSet):
    queryset = Post.objects.prefetch_related('comments').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Тот же уровень доступа, что и для V1

    def perform_create(self, serializer):
        # Автор поста автоматически связывается с текущим пользователем
        serializer.save(author=self.request.user)

    # Добавим пример дополнительной функциональности
    def list(self, request, *args, **kwargs):
        """
        Пример расширенного метода list:
        - Добавляем возможность фильтрации постов по автору.
        """
        author = request.query_params.get('author')
        if author:
            self.queryset = self.queryset.filter(author__username=author)
        return super().list(request, *args, **kwargs)

