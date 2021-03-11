from .config import LIMIT_RECENT_POSTS
from .models import Post, Tag


def get_recent_posts(limit: int = LIMIT_RECENT_POSTS):
    return Post.objects.filter(is_published=True)[:limit]


def get_all_tags():
    return Tag.objects.all()
