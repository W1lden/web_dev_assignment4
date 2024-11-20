from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    """
    Разрешение, которое позволяет редактировать объект только его автору.
    Остальным пользователям доступно только чтение.
    """
    def has_object_permission(self, request, view, obj):
        # Безопасные методы (GET, HEAD, OPTIONS) доступны всем
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Редактировать может только автор
        return obj.author == request.user
