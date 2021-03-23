from django.conf import settings
from django.db.models import Q
from django.utils import timezone

from .config import LIMIT_RECENT_POSTS
from .models import Post, Tag


def get_recent_posts(limit: int = LIMIT_RECENT_POSTS):
    return Post.objects.filter(is_published=True)[:limit]


def get_all_tags():
    return Tag.objects.all()


def get_posts(search_query):
    posts = Post.objects.filter(
        is_published=True,
        published_date__lte=timezone.localtime()
    )
    if search_query:
        data_search = search_query.strip().split(' ')
        if len(data_search) == 1:
            tag = Tag.objects.filter(name__icontains=data_search[0]).first()
            # search by tag
            if tag:
                posts = posts.filter(tags__in=[tag.pk])
            # search by title or content
            else:
                posts = posts.filter(
                    Q(title__icontains=data_search[0]) |
                    Q(content__icontains=data_search[0])
                ).distinct()
        # search by title or content
        else:
            search_query = ' '.join([item for item in data_search if item != ''])  # noqa
            posts = posts.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            ).distinct()
    return posts
