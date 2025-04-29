from django.urls import path, include
from .views import PostViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', post_list, name='post-list-create'),
    path('<int:pk>/', post_detail, name='post-detail')
]