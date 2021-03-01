from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path(
        'posts/<slug:slug>/', views.PostDetailView.as_view(),
        name='post-detail'
    ),
]
