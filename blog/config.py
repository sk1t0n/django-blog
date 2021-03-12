import os

LIMIT_RECENT_POSTS = 3
POSTS_PER_PAGE = 5
DEFAULT_POST_IMAGE = os.environ.get(
    'CLOUDINARY_DEFAULT_POST_IMAGE',
    'media/images/posts/default_qstyrv'
)
