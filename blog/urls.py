from django.urls import path

from .views import posts, tags

urlpatterns = [
    path('', posts.PostListView.as_view(), name='post-list'),
    path(
        'posts/<slug:slug>/', posts.PostDetailView.as_view(),
        name='post-detail'
    ),
    path('tags/<str:name>/', tags.PostListView.as_view(), name='tag-post-list')
]
