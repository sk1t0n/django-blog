import os

from django import template
from django.utils import timezone
from django.utils.functional import lazy

from blog.config import DEFAULT_POST_IMAGE

register = template.Library()


@register.filter(name='ru_accusative_case')
def ru_accusative_case(value: lazy) -> str:
    """Returns a word in Russian in the accusative case"""
    word = str(value)
    if word == 'статья':
        return 'статью'
    elif word == 'категория':
        return 'категорию'
    return word


@register.simple_tag
def current_year():
    return timezone.localdate().year


@register.simple_tag
def post_image(image: str = None):
    cloudinary_name = os.environ['CLOUDINARY_NAME']
    if image:
        return f'https://res.cloudinary.com/{cloudinary_name}/image/upload/v1/{image}'  # noqa
    return f'https://res.cloudinary.com/{cloudinary_name}/image/upload/v1/{DEFAULT_POST_IMAGE}'  # noqa
