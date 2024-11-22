from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Разрешение: анонимные пользователи могут только читать (GET),
    авторизованные пользователи могут добавлять, изменять и удалять.
    """
    def has_permission(self, request, view):
        # Анонимные пользователи могут только читать данные
        if request.method in SAFE_METHODS:
            return True
        # Другие действия разрешены только авторизованным
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Анонимные пользователи могут только читать
        if request.method in SAFE_METHODS:
            return True
        # Изменять и удалять могут только авторы объекта
        return obj.author == request.user
