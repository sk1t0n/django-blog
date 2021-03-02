from django import template
from django.utils.functional import lazy

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
