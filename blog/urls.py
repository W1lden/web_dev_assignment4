from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostViewSetV2

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'comments', CommentViewSet, basename='comment')

router_v2 = DefaultRouter()
router_v2.register(r'posts', PostViewSetV2, basename='post')
router_v2.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include(router_v1.urls)),
    path('v2/', include(router_v2.urls)),
]
