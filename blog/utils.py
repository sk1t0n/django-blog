import math
import re

from django.utils.html import strip_tags


def count_words_in_html(html):
    """Returns the number of words in the text"""
    text = strip_tags(html)
    matched_words = re.findall(r'\w+', text)
    count_words = len(matched_words)
    return count_words


def get_read_time(html):
    """Returns the number of minutes for which you can read the text """
    count_words = count_words_in_html(html)
    words_per_minute = 200  # Approximately the number of words per minute for the person  # noqa
    read_time_min = int(math.ceil(count_words / words_per_minute))
    return read_time_min
